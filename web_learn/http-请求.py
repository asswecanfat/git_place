import os
from flask import Flask, request
from werkzeug.datastructures import FileStorage

app = Flask(__name__)


@app.route('/', methods=['get', 'post'])
def home():
    # flask的请求对象
    print(request)
    # 获取get参数
    print(request.data)
    print(request.json)
    print(request.args)  # 获取查询字符串
    return '欢迎!'


@app.route('/form', methods=['get', 'post'])
def form():
    print(request.form)  # 表单
    print(request.files.get('file'))
    f = request.files.get('file')
    filename = f.filename
    path = f'.\\{filename}'
    f.save(path)
    size = sul_size(os.path.getsize(path))
    #print(os.path.getsize(request.files['file']))  # 接受文件
    return f'该文件共{size}大'


@app.route('/headers', methods=['get', 'post'])
def headers():
    print(request.headers)
    return 'ok'

def sul_size(size):
    if size > 1024**2:
        return f'{(size / (1024**2)):.2f}Mb'
    elif size > 1024:
        return f'{(size / 1024):.2f}Kb'
    else:
        return f'{size}b'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
