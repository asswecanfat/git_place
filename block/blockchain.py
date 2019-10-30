import hashlib
import json
import time


class BlockChain(object):  # 管理链
    def __init__(self):
        self._chain = []  # 区块链
        self._current_transactions = []  # 交易

        # 构建创世区块
        self.new_block(proof=100, previous_hash=1)

    def new_block(self, proof, previous_hash=None):
        """
        创建新的区块并加入到
        :param proof: <int>被认证的证明
        :param previous_hash: <str>上个区块的哈希值
        :return: <dict> 新的区块
        """
        block = {
            'index': len(self._chain) + 1,
            'timestamp': time.time(),
            'transactions': self._current_transactions,
            'proof': proof,
            'previous_hash': previous_hash,
        }
        # 重设交易列表
        self._current_transactions = []
        self._chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        添加交易到交易链
        :param sender: <str>发送者的地址
        :param recipient: <str>接收者的地址
        :param amount: <int>交易数量
        :return: <int>返回交易即将所在区块的index，用于提交用户的交易
        """
        self._current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """
        哈希化块(使用SHA-256)
        :param block: <dict>区块
        :return: <str>
        """
        # 必须确保字典是有序的，否则会得到不一致的哈希
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """返回区块链最后一个"""
        return self._chain[-1]

    def proof_of_work(self, last_proof):
        """
        简单的工作证明算法:
            - 找到一个数字a使得hash(ab)得到的字符串后四位(自定义)是0
            - b是上一个区块的proof，a是找到的proof
        :param last_proof: <int>
        :return: <int>
        """
        proof = 0
        while self.valid_proof(last_proof, proof):
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        通过hash(last_proof, proof)计算出的字符串尾部是否有4个0
        :param last_proof: <int>上一个的区块证明
        :param proof: <int>现在的证明
        :return: <bool>是否包含4个0
        """
        guess_hash = hashlib.sha256(f'{last_proof}{proof}'.encode()).hexdigest()
        return guess_hash[-4] == '0000'

    def get_chain(self):
        return self._chain

    def __repr__(self):
        return f'{self.__class__.__name__!r}()'
