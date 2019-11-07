from flask import Flask, request, jsonify, redirect, url_for, make_response


app = Flask(__name__)


@app.route('/', methods=['get', 'post'])
def home():
    return '<a href="https://www.baidu.com" target="blank_">click</a>'


@app.route('/tt', methods=['get'])
def tt():
    # 返回json数据
    data = [
        {'name': '??', 'age': 18},
        {'name': '???', 'age': 19},
        {'name': '????', 'age': 20},
    ]
    return jsonify(data)


@app.route('/re', methods=['get', 'post'])
def re():
    # 重定向
    print(request)
    return redirect('https://www.baidu.com')


@app.route('/ret', methods=['get', 'post'])
def ret():
    # 跳转到站内的函数
    # url_for与函数一致，就算路由改动也无需改动函数，可接受参数
    return redirect(url_for('re'))  # return redirect('/re')若路由改动它也改


@app.route('/tes', methods=['get'])
def tes():
    # 返回自定义状态码或自定义响应信息
    reponse = make_response()
    reponse.headers['T'] = 'no'
    return reponse, 205  # 自定义状态码


if __name__ == '__main__':
    app.run(debug=True)
