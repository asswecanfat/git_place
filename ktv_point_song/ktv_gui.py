import PySimpleGUI as sg


def main_win(dbase, u_id, user_name):
    song_list = []
    cash = {}  # 歌名与id缓存
    f_b1 = sg.Radio('按歌手全称搜索', None, default=True)
    f_b2 = sg.Radio('按歌手简称搜索', None)
    f_b3 = sg.Radio('按歌名全称搜索', None)
    f_b4 = sg.Radio('按歌名简称搜索', None)
    find_func = {
        f_b1: lambda d, v: _find_data(d, v, 'singer'),
        f_b2: lambda d, v: _find_data(d, v, 'singer_py'),
        f_b3: lambda d, v: _find_data(d, v, 'song'),
        f_b4: lambda d, v: _find_data(d, v, 'song_py'),
    }
    rank = sg.Listbox(values=[], disabled=True, size=(40, 22), auto_size_text=True)
    find = sg.Listbox(values=[], select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED, size=(40, 19))
    song = sg.Listbox(values=[], size=(40, 20), select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED)
    c_v, n_cash = _get_collection(dbase, u_id)
    cash.update(n_cash)
    collection = sg.Listbox(values=c_v,
                            size=(40, 20),
                            select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED)
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
    # 框架4
    layout4 = [[sg.Text('已收藏：')],
               [collection],
               [sg.Button('加入歌单'), sg.Button('取消收藏')]]
    frame4 = sg.Frame(title=None, layout=layout4)

    # 整合
    layout = [[frame1, frame4, frame2, frame3],
              ]
    window = sg.Window(f'欢迎用户：{user_name}来到ktv点歌系统！！', layout)

    while True:
        event, values = window.read()
        print(values)
        if event is None:
            break
        if event == '查找':
            for key in find_func.keys():
                if key.get():
                    song_data, new_values = find_func[key](dbase, values[2])
                    cash.update(song_data)
                    find.update(values=new_values)
        if event == '点歌':
            length = len(song_list)
            for num, vl in enumerate(values[7]):
                sname = vl.split(".")[1]
                song_list.append(f'{length + num + 1}.{sname}')
                dbase.update_rank(sname.split('-')[0])
        if event == '置顶':
            for x in values[-1]:
                song_list.remove(x)
            song_list = [*values[-1], *song_list]
            song_list = [f'{num + 1}.{vl.split(".")[1]}' for num, vl in enumerate(song_list)]
        if event == '删除':
            for i in values[-1]:
                song_list.remove(i)
            song_list = [f'{num + 1}.{vl.split(".")[1]}' for num, vl in enumerate(song_list)]
        if event == '收藏':
            for i in values[-2]:
                v = i.split('-')[0].split('.')[1]
                if not dbase.add_collections(u_id, cash.get(v)):
                    sg.popup('连接网络出错！', title='提示')
                    break
        if event == '加入歌单':
            length = len(song_list)
            for num, vl in enumerate(values[1]):
                sname = vl.split(".")[1]
                song_list.append(f'{length + num + 1}.{sname}')
                dbase.update_rank(sname.split('-')[0])
        if event == '取消收藏':
            for i in values[1]:
                if not dbase.delete_collection(u_id, cash[i.split('-')[0].split('.')[1]]):
                    sg.popup('连接网络出错！', '提示')
                    break
        collection_v, up_cash = _get_collection(dbase, u_id)
        cash.update(up_cash)
        rank_v = _get_rank_data(dbase)

        collection.update(values=collection_v)
        rank.update(disabled=False, values=rank_v)
        rank.update(disabled=True)

        song.update(values=song_list)
        window.refresh()
        print(cash)
    window.close()


def _get_rank_data(dbase):
    rank_data = dbase.get_rank_data()
    rank_v = [f'{num + 1}.{vl[0]}-----{vl[1]}----点击数:{vl[2]}' for num, vl in enumerate(rank_data)]
    return rank_v


def _find_data(dbase, values, by_what):
    data = dbase.find_data_by(by_what, values)
    new_values = [f'{num + 1}.{va[1]}------{str(va[2])}' for num, va in enumerate(data)]
    return {i[1]: i[0] for i in data}, new_values


def _get_collection(dbase, u_id):
    result, data = dbase.deal_sql(sql='select so_name,s_name,son_id from collection,song,singer '
                                      f'where collection.u_id={u_id} and collection.son_id=song.song_id '
                                      f'and song.singer_i=singer.singer_id')
    values = [f'{num + 1}.{va[0]}------{str(va[1])}' for num, va in enumerate(data)]
    return values, {i[0]: i[2] for i in data}


if __name__ == '__main__':
    from db import DBMethod

    with DBMethod(user='root', password='123456', db='ktv_song') as db:
        main_win(db)
