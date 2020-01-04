import PySimpleGUI as sg
from regiser_ui import reg_ui
from ktv_gui import main_win as ktv_ui
from sys_manger_ui import main_m_ui as manger_ui


def main_gui(db):
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
        if event == '登录':
            try:
                user, user_id = __reg(values[0], values[1], db)
                if user is not None:
                    sg.popup(f'用户{user}登录成功!!', title='提示')
                    if user_id is not None:
                        window.close()
                        ktv_ui(db, user_id, user)
                    else:
                        window.close()
                        manger_ui(db)
                    break
                else:
                    sg.popup('登录失败!!', title='提示')
            except BaseException as e:
                # print(e)
                sg.popup('密码错误', title='提示')
        if event == '注册':
            user = reg_ui(db)
            get_username.update(user if user else '')
            window.refresh()
    db.close()
    window.close()


def __reg(user, password, db):
    result, data = db.deal_sql(sql='select user_name,u_password,user_id from ktv_user')
    adm_res, admin = db.deal_sql(sql='select admin,admin_password from administrators')
    if result and adm_res:
        login_data = {i[0]: (i[1], i[2]) for i in data}
        admin_data = {i[0]: i[1] for i in admin}
        if user in login_data.keys():
            if password == login_data[user][0]:
                return user, login_data[user][1]
        elif user in admin_data.keys():
            if password == admin_data[user]:
                return '管理员', None
        raise BaseException('密码错误')
    return None


if __name__ == '__main__':
    from db import DBMethod
    dbase = DBMethod(host='*****', user='***', password='***', db='ktv_song')
    main_gui(dbase)
