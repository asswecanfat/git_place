from flask import Flask, render_template
from config import Config


app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)


@app.route('/', methods=['get', 'post'])
def home():
    # return render_template('模块路径', 变量=数据)
    data = [
        {'id': 1, 'name': 'ass', 'age': 18},
    ]
    d = {}
    d['d'] = [{'id': 1, 'name': 'ass', 'age': 18},]
    d['title'] = 'yes'
    # return render_template('www.html', title='yes', data=data)
    return render_template('www.html', **d)


if __name__ == '__main__':
    app.run(debug=True)
