from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)


@app.route('/home/<int:pages>')
def to(pages):
    return '你被发现了！！'


# 自定义路由转换器
class Mobile(BaseConverter):
    regex = r'\d{11}'


app.url_map.converters['Mobile'] = Mobile  # 加入规则


@app.route('/sms/<Mobile:m>')
def sms(m):
    return f'你的电话:{m}'


class Regx(BaseConverter):
    """正则表达式路由转换器"""

    def __init__(self, url_map, *args):
        super().__init__(url_map)
        self.regex = args[0]


app.url_map.converters['re'] = Regx


@app.route(r'/te/<re(r".+"):rep>')
def te(rep):
    return rep


@app.route('/t/<uuid:name>')
def t(name):
    print(name)
    return 'ok'


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
