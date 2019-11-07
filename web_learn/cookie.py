from flask import Flask, make_response, request


app = Flask(__name__)


@app.route('/setc', methods=['get', 'post'])
def set_cookie():
    response = make_response('设置cookie')
    # response.set_cookie('变量名', '变量值', max_age=有效期)
    response.set_cookie('username', '123', max_age=2)
    return response


@app.route('/getc', methods=['get', 'post'])
def get_cookie():
    u_name = request.cookies.get('username')
    return f'<h1>用户名为{u_name}</h1>'



if __name__ == '__main__':
    app.run(debug=True)