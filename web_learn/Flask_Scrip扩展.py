from flask import Flask
from flask_script import Manager, Command  # 通过命令行启动  # 自定义命令
from web_learn.config import Config


app = Flask(__name__)
man = Manager(app)


app.config.from_object(Config)

@app.route('/', methods=['get', 'post'])
def home():
    return 'ok'


class HelloCom(Command):
    """
        命令行终端描述
    """
    def run(self):
        print('这里是终端')


man.add_command('hello', HelloCom)


if __name__ == '__main__':
    man.run(default_command='runserver')
