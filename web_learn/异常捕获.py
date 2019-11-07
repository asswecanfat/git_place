from flask import Flask, abort
from web_learn.config import Config


app = Flask(__name__)

app.config.from_object(Config)


@app.route('/', methods=['get', 'post'])
def home():
    abort(404)  # 抛出异常，继承reponse类
    return '<h1>Home</h1>'


@app.errorhandler(404)  # 可以是码，也可以是异常类
def error_404(error):  # 异常的捕获和处理
    return '<h1>404：未找到页面</h1>'


if __name__ == '__main__':
    app.run(debug=True)
