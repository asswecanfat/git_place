from flask import Flask, current_app, g
# current_app类似于self，只能用于视图中, g是全局变量
"""
    请求上下文：保存了客户端和服务器交互的数据
    应用上下文：flask应用程序运行过程中，保存的一些配置文件，如程序名，数据库连接，和应用信息
"""
from web_learn.config import Config


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['get', 'post'])
def home():
    g.name = 'ass'
    func()
    print(app)
    print(current_app)  # 用于视图
    return 'ok'


def func():
    print(f'yes!{g.name}')


if __name__ == '__main__':
    app.run(debug=True)