import PySimpleGUI as sg


class Sys:
    def __int__(self, values, title):
        self.listBox = sg.Listbox(values=values,
                                  auto_size_text=True,
                                  size=(40, 22),
                                  select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED)
        self.title = sg.Text(title)
        self.add_button = sg.Button('增加')
        self.delete_button = sg.Button('删除')
        self.change_button = sg.Button('修改')
        self.find_button = sg.Button('查找')
        self.frame = sg.Frame(None, [[self.title],
                                     [self.listBox],
                                     [self.add_button,
                                      self.delete_button,
                                      self.change_button,
                                      self.find_button, ]])

    def get_frame(self):
        return self.frame

    def update(self, values):
        self.listBox.update(values)

    def add(self):  # 增
        pass

    def delete(self):  # 删
        pass

    def change(self):  # 改
        pass

    def find(self):  # 查
        pass


class User(Sys):
    def __init__(self, db):
        super().__int__(values=_get_user(db), title='用户列表')

    def add(self):
        pass

    def delete(self):
        pass

    def change(self):
        pass

    def find(self):
        pass


class Song(Sys):
    def __init__(self, db):
        super().__int__(values=_get_song(db), title='歌曲列表')

    def add(self):
        pass

    def delete(self):
        pass

    def change(self):
        pass

    def find(self):
        pass


class Singer(Sys):
    def __init__(self, db):
        super().__int__(values=_get_singer(db), title='歌手列表')

    def add(self):
        pass

    def delete(self):
        pass

    def change(self):
        pass

    def find(self):
        pass


def main_m_ui(db):
    user = User(db)
    song = Song(db)
    singer = Singer(db)
    # 组件
    user_frame = user.get_frame()
    song_frame = song.get_frame()
    singer_frame = singer.get_frame()
    # 布局
    layout = [[user_frame, song_frame, singer_frame]]
    window = sg.Window('管理员系统', layout)

    while True:
        event, values = window.read()
        if event is None:
            break


def _get_user(db) -> list:

    return [1, 2, 3]


def _get_song(db) -> list:
    return [3, 2, 1]


def _get_singer(db) -> list:
    return [1, 2, 3]


if __name__ == '__main__':
    from db import DBMethod

    dbase = DBMethod(user='root', password='123456', db='ktv_song')

    main_m_ui(dbase)
