import PySimpleGUI as sg
import re
from datetime import datetime


class Sys:
    def __int__(self, values, title, head):
        self.table = sg.Table(values=values,
                              headings=head,
                              size=(50, 25),
                              enable_events=True,
                              select_mode=sg.TABLE_SELECT_MODE_EXTENDED)
        self.title = sg.Text(title)
        self.add_button = sg.Button('增加')
        self.delete_button = sg.Button('删除')
        self.change_button = sg.Button('修改')
        self.find_button = sg.Button('查找')
        self.frame = sg.Frame(None, [[self.title],
                                     [self.table],
                                     [self.add_button,
                                      self.delete_button,
                                      self.change_button,
                                      self.find_button, ]])

    def get_frame(self):
        return self.frame

    def add(self):  # 增
        pass

    def delete(self):  # 删
        pass

    def change(self):  # 改
        pass

    def find(self):  # 查
        pass


class User(Sys):
    # 增，删，改，查
    def __init__(self, db, cash):
        super().__int__(values=cash, title='用户列表', head=['用户id',
                                                         '用户名',
                                                         '用户密码',
                                                         '用户真名',
                                                         '用户性别',
                                                         '注册时间'])
        self.db = db

    def add(self):
        text = sg.popup_get_text('请输入用户名，用户密码，用户真名，性别，修改原因(数据之间用,隔开)：')
        value = re.split(r'[,，]', text if text is not None else '')
        try:
            if self.db.add_user(value[0], value[1], value[2], value[3]):
                result, length = self.db.deal_sql('select count(*) from logging')
                deal_id = length[0][0] + 1
                time = re.sub(r'\.\d+', '', str(datetime.today()))
                if self.db.insert_sql(f"insert into logging values('{deal_id}','{value[0]}"
                                      f"添加','{time}','admin','{value[4]}')"):
                    sg.popup(f'添加用户:{value[0]}成功!', title='提示')

        except IndexError:
            sg.popup('输入有误！', title='错误')
        finally:
            self.table.update(values=_get_data(self.db, 'ktv_user'))

    def delete(self):
        pass

    def change(self):
        pass

    def find(self):
        pass


class Song(Sys):
    # 增0，删1，改2，查3
    def __init__(self, db, cash):
        super().__int__(values=cash, title='歌曲列表', head=['歌曲id',
                                                         '歌曲名',
                                                         '歌手id',
                                                         '歌曲语言',
                                                         '歌曲类型',
                                                         '歌曲简写',
                                                         '歌曲长度'])
        self.db = db

    def add(self):
        pass

    def delete(self):
        pass

    def change(self):
        pass

    def find(self):
        pass


class Singer(Sys):
    # 增4，删5，改6，查7
    def __init__(self, db, cash):
        super().__int__(values=cash, title='歌手列表', head=['歌手id',
                                                         '歌手名字',
                                                         '歌手性别',
                                                         '歌手所属地',
                                                         '歌手类型',
                                                         '拼音缩写',
                                                         '归属地'])
        self.db = db

    def add(self):
        pass

    def delete(self):
        pass

    def change(self):
        pass

    def find(self):
        pass


def main_m_ui(db):
    try:
        user = User(db, _get_data(db, 'ktv_user'))
        song = Song(db, _get_data(db, 'song'))
        singer = Singer(db, _get_data(db, 'singer'))

        # 组件
        user_frame = user.get_frame()
        song_frame = song.get_frame()
        singer_frame = singer.get_frame()
        # 布局
        layout = [[user_frame, song_frame, singer_frame]]
        window = sg.Window('管理员系统', layout)

        while True:

            event, values = window.read()
            print(event)
            print(values)
            if event is None:
                break
            if event == '增加':
                user.add()
            window.refresh()
        window.close()
    except ConnectionError:
        print('出错')


def _get_data(db, key) -> list:
    result, data = db.deal_sql(f'select * from {key}')
    if not result:
        raise ConnectionError
    return [list(i) for i in data]


if __name__ == '__main__':
    from db import DBMethod

    dbase = DBMethod(user='root', password='123456', db='ktv_song')

    main_m_ui(dbase)
