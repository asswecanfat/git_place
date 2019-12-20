import PySimpleGUI as sg
from db import DBMethod
from regiser_ui import reg_ui


dbase = DBMethod(user='root', password='123456', db='ktv_song')


def main_gui():
    # 组件
    username = sg.Text('用户名：')
    password = sg.Text('密码：')
    get_username = sg.Input()
    get_password = sg.Input(password_char='*')

    l1 = [[username],
          [password]]
    frame1 = sg.Frame(None, layout=l1, element_justification='right', relief=sg.RELIEF_FLAT)

    l2 = [[get_username],
          [get_password]]
    frame2 = sg.Frame(None, layout=l2, relief=sg.RELIEF_FLAT)
    # 布局
    layout = [[frame1, frame2],
              [sg.Button('登录'), sg.Button('注册')]]
    window = sg.Window('登录', layout)

    while True:
        event, values = window.read()
        if event is None:
            break
        if event is '登录':
            try:
                user = __reg(values[0], values[1])
                if user is not None:
                    sg.popup(f'用户{user}登录成功!!', title='提示')
                else:
                    sg.popup('登录失败!!', title='提示')
            except BaseException:
                sg.popup('密码错误', title='提示')
        if event is '注册':
            user = reg_ui(dbase)
            get_username.update(user if user else '')
            window.refresh()
    dbase.close()
    window.close()


def __reg(user, password):
    result, data = dbase.deal_sql(sql='select user_name,u_password from ktv_user')
    adm_res, admin = dbase.deal_sql(sql='select admin,admin_password from administrators')
    if result:
        login_data = {i[0]: i[1] for i in data}
        admin_data = {i[0]: i[1] for i in admin}
        if user in login_data.keys():
            if password == login_data[user]:
                return user
            raise BaseException('密码错误')
        elif user in admin_data.keys():
            if password == admin_data[user]:
                return '管理员'
            raise BaseException('密码错误')
    return None


if __name__ == '__main__':
    main_gui()
