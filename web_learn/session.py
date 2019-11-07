from flask import Flask, session
import random
import base64

app = Flask(__name__)


# 声明配置类
class Config:
    SECRET_KEY = base64.b64encode(bytes(random.randint(100000, 19999999)))


# 加载配置
app.config.from_object(Config)


@app.route('/ses', methods=['get', 'post'])
def set_session():
    session['username'] = '123'
    return 'ok'


@app.route('/ges', methods=['get', 'post'])
def get_session():
    name = session.get('')
    return f'<h1>name:{name}</h1>'


if __name__ == '__main__':
    app.run(debug=True)
