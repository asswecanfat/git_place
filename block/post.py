import requests


def post_data(sender, recipient, amount):
    data = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount,
    }
    requests.post('http://127.0.0.1:5000/transactions/new', json=data)


if __name__ == '__main__':
    _sender = input('请输入发送者：')
    _recipient = input('请输入接收者：')
    _amount = input('请输入交易数目：')
    post_data(_sender, _recipient, _amount)
