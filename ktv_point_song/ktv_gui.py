import PySimpleGUI as sg


def main_win(dbase):
    global song_list
    f_b1 = sg.Radio('按歌手全称搜索', None, default=True)
    f_b2 = sg.Radio('按歌手简称搜索', None)
    f_b3 = sg.Radio('按歌名全称搜索', None)
    f_b4 = sg.Radio('按歌名简称搜索', None)
    find_func = {
        f_b1: lambda d, v, f, w: _find_data(d, v, f, w, 'singer'),
        f_b2: lambda d, v, f, w: _find_data(d, v, f, w, 'singer_py'),
        f_b3: lambda d, v, f, w: _find_data(d, v, f, w, 'song'),
        f_b4: lambda d, v, f, w: _find_data(d, v, f, w, 'song_py'),
    }
    rank = sg.Listbox(values=[], disabled=True, size=(40, 22), auto_size_text=True)
    find = sg.Listbox(values=[], select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED, size=(40, 19))
    song = sg.Listbox(values=[], size=(40, 20), select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED)
    pyin = sg.Input()
    # 框架1
    layout1 = [[sg.Text('今日排行：')],
               [rank], ]
    frame1 = sg.Frame(title=None, layout=layout1)

    # 框架2
    layout2 = [[sg.Text('请输入歌手/歌名(均可简写)：')],
               [pyin],
               [f_b1, f_b2],
               [f_b3, f_b4],
               [find],
               [sg.Button('查找'), sg.Button('点歌'), sg.Button('收藏')]]
    frame2 = sg.Frame(title=None, layout=layout2)

    # 框架3
    layout3 = [[sg.Text('已选歌曲：')],
               [song],
               [sg.Button('置顶'), sg.Button('删除')]]
    frame3 = sg.Frame(title=None, layout=layout3)
    # 整合
    layout = [[frame1, frame2, frame3],
              ]
    window = sg.Window('欢迎来到ktv点歌系统！！', layout)

    while True:
        event, values = window.read()
        print(values)
        if event is None:
            break
        if event is '查找':
            for key, value in find_func.items():
                if key.get():
                    value(dbase, values, find, window)
        if event is '点歌':
            length = len(song_list)
            for num, vl in enumerate(values[6]):
                sname = vl.split(".")[1]
                song_list.append(f'{length + num + 1}.{sname}')
                db.update_rank(sname.split('-')[0])
        if event is '置顶':
            for x in values[-1]:
                song_list.remove(x)
            song_list = [*values[-1], *song_list]
            song_list = [f'{num + 1}.{vl.split(".")[1]}' for num, vl in enumerate(song_list)]
        if event is '删除':
            for i in values[-1]:
                song_list.remove(i)
            song_list = [f'{num + 1}.{vl.split(".")[1]}' for num, vl in enumerate(song_list)]
        _get_rank_data(rank, window, dbase)
        song.update(values=song_list)
        window.refresh()
    window.close()


def _get_rank_data(rank, window, dbase):
    rank_data = dbase.get_rank_data()
    rank_v = [f'{num + 1}.{vl[0]}-----{vl[1]}----点击数:{vl[2]}' for num, vl in enumerate(rank_data)]
    rank.update(disabled=False, values=rank_v)
    rank.update(disabled=True)
    window.refresh()


def _find_data(dbase, values, find, window, by_what):
    data = dbase.find_data_by(by_what, values[1])
    get_valuse = [f'{num + 1}.{va[0]}------{str(va[1])}' for num, va in enumerate(data)]
    find.update(values=get_valuse)
    window.refresh()


if __name__ == '__main__':
    from db import DBMethod
    song_list = []
    with DBMethod(user='root', password='123456', db='ktv_song') as db:
        main_win(db)
