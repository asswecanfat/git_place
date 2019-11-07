from flask import Flask, render_template
from config import Config


app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)

@app.template_filter('mobile')
def mo(data, string):
    return data[:4] + string + data[7:]


@app.route('/', methods=['get', 'post'])
def home():
    # return render_template('模块路径', 变量=数据)
    data = {}
    data['list'] = [
        {'id': 1, 'phone': '15521318232', 'age': 18},
    ]
    data['content'] = '<h1>hello world</h1>'
    return render_template('index3.html', **data)


if __name__ == '__main__':
    app.run(debug=True)
