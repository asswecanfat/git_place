from flask import Flask, render_template
from config import Config


app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)


@app.route('/', methods=['get', 'post'])
def home():
    # return render_template('模块路径', 变量=数据)
    data = {}
    data['data'] = [
        {'id': 1, 'name': 'ass', 'age': 18},
        {'id': 2, 'name': 'as', 'age': 19},
        {'id': 3, 'name': 'a', 'age': 20},
    ]
    data['content'] = '<h1>hello world</h1>'
    return render_template('index2.html', **data)


if __name__ == '__main__':
    app.run(debug=True)
