import PySimpleGUI as sg


def reg_ui(dba):
    # 组件
    title = sg.Text('注册', justification='center')
    u = sg.Text('用户名：')
    r_n = sg.Text('姓名：')
    s = sg.Text('性别：')
    p = sg.Text('密码：')
    e = sg.Text('确认密码：')

    user_name = sg.Input()
    real_name = sg.Input()
    sex1 = sg.Radio('男', 1, default=True)
    sex2 = sg.Radio('女', 1)
    password = sg.Input(password_char='*')
    ensure_p = sg.Input(password_char='*')

    enter_ok = sg.Button('注册')
    enter_cancle = sg.Button('取消')
    # 框架
    f2 = sg.Frame(None, [[u], [r_n], [s], [p], [e]])
    f3 = sg.Frame(None, [[user_name], [real_name], [sex1, sex2], [password], [ensure_p]])
    # 布局
    layout = [[title],
              [f2, f3],
              [enter_ok, enter_cancle]]
    window = sg.Window('注册', layout)
    while True:
        event, values = window.read()
        if event in (None, '取消'):
            break
        if event is '注册':
            if values[4] == values[5]:
                reslut = dba.add_user(user_name=values[0],
                                      u_password=values[4],
                                      real_name=values[1],
                                      u_sex='男' if values[2] else '女'
                                      )
                if reslut:
                    sg.popup('注册成功！')
                    break
                else:
                    sg.popup('用户已存在!')
            else:
                sg.popup('密码不一致！')
    window.close()
    return values[0]


if __name__ == '__main__':
    from login import dbase
    reg_ui(dbase)
