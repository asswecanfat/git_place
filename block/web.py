from flask import Flask, render_template, request, jsonify
from uuid import uuid4
from blockchain import BlockChain


app = Flask(__name__)
block_chain = BlockChain()
node_identifier = str(uuid4()).replace('-', '')


@app.route('/', methods=['get', 'post'])
def home():
    data = {'title': '欢迎来到TT币圈！', 'url': {
        'transactions': '/transactions/new',
        'mine': '/mine',
        'chain': '/chain',
    }}
    return render_template('www.html', **data)


@app.route('/transactions/new', methods=['post'])
def new_transactions():
    values = request.get_json()
    required = ('sender', 'recipient', 'amount')
    if not all(i in values for i in required):
        return '<h1>值缺失</h1>', 400
    index = block_chain.new_transaction(sender=values['sender'],
                                        recipient=values['recipient'],
                                        amount=values['amount'])
    response = {'message': f'交易将会加入到区块{index}中'}
    return jsonify(response), 201


@app.route('/mine', methods=['get'])
def mine():
    last_block = block_chain.last_block
    last_proof = last_block['proof']
    proof = block_chain.proof_of_work(last_proof)
    block_chain.new_transaction(
        sender='0',
        recipient=node_identifier,
        amount=1,
    )
    previous_hash = block_chain.hash(last_block)
    block = block_chain.new_block(proof, previous_hash)
    response = {
        'message': '新的区块建立了',
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200


@app.route('/chain', methods=['get'])
def chain():
    response = {
        'chain': block_chain.get_chain(),
        'length': len(block_chain.get_chain()),
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(debug=True)
