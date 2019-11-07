from flask import Flask
from web_learn.config import Config


app = Flask(__name__)


app.config.from_object(Config)


@app.before_first_request  # 初始化数据库的时候
def fuck():
    print('开始')


@app.before_request  # 每次请求前
def fu():
    print('每次前')


@app.after_request
def ad(reponse):
    reponse = reponse
    print(reponse)
    print('每次请求后')
    return reponse


@app.teardown_request  # 接收一个异常，便于发现视图的问题
def gg(error):  # 需要在debug为false下启用
    print(error)
    print('进入debug')


@app.route('/', methods=['get', 'post'])
def home():
    return 'Home'


if __name__ == '__main__':
    app.run()