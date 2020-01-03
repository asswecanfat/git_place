import PySimpleGUI as sg
import re
from datetime import datetime, time as ntime


class Sys:
    def __init__(self, values, title, head, db):
        self.table = sg.Table(values=values,
                              headings=head,
                              size=(50, 25),
                              enable_events=True,
                              )
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
        self.db = db
        self.index = None
        self._data = self.table.get()
        self._lable = None
        self._db_table = None
        self._table_id = None

    def update_index(self, index):
        self.index = index

    def get_frame(self):
        return self.frame

    def add(self):  # 增
        self.table.update(values=_get_data(self.db, self._db_table))
        self._data = self.table.get()

    def delete(self):  # 删
        delete_data = self._data[self.index]
        try:
            if self.db.insert_delete_sql(f'delete from {self._db_table} where {self._table_id}=%(value)s',
                                         {'value': delete_data[0]}):
                remark = sg.popup_get_text('请输入删除的理由：')
                insert_logging(self.db, str(delete_data[1]), action='删除', remark=remark)
                sg.popup(f'{self._lable}：{delete_data[1]}(id：{delete_data[0]})删除成功！', title='提示')
            else:
                sg.popup('删除失败！', title='提示')
        except IndexError:
            sg.popup(f'请选择{self._lable}！', title='提示')
        finally:
            self.table.update(values=_get_data(self.db, self._db_table))
            self._data = self.table.get()

    def change(self):  # 改
        if self.index:
            self.table.update(values=_get_data(self.db, self._db_table), select_rows=[self.index])
        else:
            self.table.update(values=_get_data(self.db, self._db_table))
        self._data = self.table.get()

    def find(self):  # 查
        value = sg.popup_get_text(f'请输入{self._lable}名：')
        sure = False
        for num, data in enumerate(self._data):
            if data[1] == value:
                self.table.update(select_rows=[num])
                sure = True
                break
        if not sure:
            self.table.update(select_rows=[])
            sg.popup(f'无此{self._lable}信息！', title='提示')

    def _return_right(self, data, source):
        return data if data else source


def insert_logging(db, value, action=None, remark=None) -> bool:
    result, length = db.deal_sql('select count(*) from logging')
    deal_id = length[0][0] + 1
    time = re.sub(r'\.\d+', '', str(datetime.today()))
    if db.insert_delete_sql(f'insert into logging values(%(deal_id)s,%(deal)s,%(deal_time)s,'
                            f'%(deal_people)s,%(remarks)s)', {'deal_id': deal_id,
                                                              'deal': value + action,
                                                              'deal_time': time,
                                                              'deal_people': 'admin',
                                                              'remarks': remark}
                            ):
        return True
    return False


class User(Sys):
    # 增，删，改，查
    def __init__(self, db, cash):
        super().__init__(values=cash, title='用户列表', head=['用户id',
                                                          '用户名',
                                                          '用户密码',
                                                          '用户真名',
                                                          '用户性别',
                                                          '注册时间'], db=db)
        self._lable = '用户'
        self._db_table = 'ktv_user'
        self._table_id = 'user_id'

    def add(self):
        text = sg.popup_get_text('请输入用户名，用户密码，用户真名，性别，修改原因(数据之间用,隔开)：')
        value = re.split(r'[,，]', text if text is not None else '')
        try:
            if self.db.add_user(value[0], value[1], value[2], value[3]):
                insert_logging(self.db, str(value[0]), action='添加', remark=value[4])
                sg.popup(f'添加用户:{value[0]}成功!', title='提示')
            else:
                sg.popup('添加失败！', title='提示')
        except IndexError:
            sg.popup('输入有误！', title='错误')
        finally:
            super().add()

    def change(self):
        try:
            source_data = self._data[self.index]
            user_name = sg.popup_get_text('请输入要修改的用户名(无输入为不修改)：')
            user_password = sg.popup_get_text('请输入要修改的用户对应的密码(无输入为不修改)：')
            user_real_name = sg.popup_get_text('请输入要修改的用户真名(无输入为不修改)：')
            user_sex = sg.popup_get_text('请输入要修改的用户性别(无输入为不修改)：')
            remark = sg.popup_get_text('请输入修改理由：')  # user_sex if user_sex else source_data[4]
            sql = f"update ktv_user set user_name='{self._return_right(user_name, source_data[1])}'," \
                  f"u_password='{self._return_right(user_password, source_data[2])}'," \
                  f"real_name='{self._return_right(user_real_name, source_data[3])}'," \
                  f"u_sex='{self._return_right(user_sex, source_data[4])}' " \
                  f"where user_id='{source_data[0]}'"
            if self.db.change(sql):
                insert_logging(self.db,
                               f'用户{self._return_right(user_name, source_data[1])}(原用户{source_data[1]})',
                               action='修改', remark=remark)
                sg.popup('修改成功！', title='提示')
            else:
                sg.popup('修改失败！', title='提示')
        except TypeError:
            sg.popup('未选择用户！', title='提示')
        finally:
            super().change()


class Song(Sys):
    # 增0，删1，改2，查3
    def __init__(self, db, cash):
        super().__init__(values=cash, title='歌曲列表', head=['歌曲id',
                                                          '歌曲名',
                                                          '歌手id',
                                                          '歌曲语言',
                                                          '歌曲类型',
                                                          '歌曲简写',
                                                          '歌曲长度'], db=db)
        self._lable = '歌曲'
        self._db_table = 'song'
        self._table_id = 'song_id'

    def add(self):
        text = sg.popup_get_text('请输入歌曲名,歌手名,歌曲语言,类型,简写,长度,修改原因(数据之间用,隔开)：')
        value = re.split(r'[,，]', text if text is not None else '')
        song_num_sql = 'select count(*) from song'
        singer_id_sql = 'select singer_id from singer where s_name=%(s_name)s'
        add_sql = 'insert into song values(%(song_id)s,%(song_name)s,%(singer_id)s,%(language)s,' \
                  '%(type)s,%(short_name)s,%(length)s)'
        try:
            nresult, song_num = self.db.deal_sql(song_num_sql)
            result, singer_id = self.db.deal_sql(singer_id_sql, {'s_name': value[1]})
            source_time = value[5].split(':')
            song_id = song_num[0][0] + 1 if song_num[0] else None
            time = ntime(int(source_time[0]), int(source_time[1]), int(source_time[-1]))
            if singer_id[0] and song_id:
                if self.db.add(add_sql, {'song_id': song_id, 'song_name': value[0], 'singer_id': singer_id,
                                         'language': value[2], 'type': value[3],
                                         'short_name': value[4], 'length': time}):
                    insert_logging(self.db, str(value[0]), action='添加', remark=value[4])
                    sg.popup(f'添加歌曲:{value[0]}成功!', title='提示')
                else:
                    raise BaseException
            else:
                sg.popup('网络出错！', title='提示')
        except IndexError:
            sg.popup('无该歌手！', title='错误')
        except BaseException as e:
            print(e)
            sg.popup('添加失败！', title='提示')
        finally:
            super().add()

    def change(self):
        singer_id_sql = 'select singer_id from singer where s_name=%(singer_name)s'
        change_sql = 'update song set so_name=%(song_name)s,singer_i=%(singer_id)s,' \
                     'languages=%(language)s,song_type=%(song_type)s,song_py=%(song_py)s,' \
                     'song_length=%(song_length)s where song_id=%(song_id)s'
        try:
            source_data = self._data[self.index]
            values = self._change_input()  # values[4] if values[4] else source_data[5]}
            *result, singer_id = self.db.deal_sql(singer_id_sql, {'singer_name': values[1]}) if values[1] else \
                [source_data[2]]
            soup = values[-2]
            time = ntime(soup[0], soup[1], soup[2]) if soup else source_data[-1]
            if not singer_id:
                raise NameError
            if self.db.change(change_sql, {'song_name': self._return_right(values[0], source_data[1]),
                                           'singer_id': singer_id[0],
                                           'language': self._return_right(values[2], source_data[3]),
                                           'song_type': self._return_right(values[3], source_data[4]),
                                           'song_py': self._return_right(values[4], source_data[5]),
                                           'song_length': time,
                                           'song_id': source_data[0]}):
                insert_logging(self.db, str(values[0]), action='修改', remark=values[-1])
                sg.popup(f'歌曲:{values[0]}(原名:{source_data[1]}修改成功！)', title='提示')
            else:
                sg.popup('修改失败！', title='提示')
        except TypeError as e:
            print(e)
            sg.popup('未选择歌曲！', title='提示')
        except NameError:
            sg.popup('无该歌手！', title='提示')
        finally:
            super().change()

    def _change_input(self) -> list:
        song_name = sg.popup_get_text('请输入要修改的歌曲名(无输入为不修改)：')
        singer_name = sg.popup_get_text('请输入要修改的歌手名(无输入为不修改)：')
        language = sg.popup_get_text('请输入要修改的语言(无输入为不修改)：')
        song_type = sg.popup_get_text('请输入要修改的歌曲类型(无输入为不修改)：')
        song_short_name = sg.popup_get_text('请输入要修改的简称(无输入为不修改)：')
        song_length = sg.popup_get_text('请输入要修改的歌曲时长(无输入为不修改)：')
        remark = sg.popup_get_text('请输入修改理由：')
        # soup = self._return_right(song_length.split(':'), )
        return [song_name, singer_name, language, song_type, song_short_name,
                song_length, remark]


class Singer(Sys):
    # 增4，删5，改6，查7
    def __init__(self, db, cash):
        super().__init__(values=cash, title='歌手列表', head=['歌手id',
                                                          '歌手名字',
                                                          '歌手性别',
                                                          '歌手所属国',
                                                          '歌手类型',
                                                          '拼音缩写',
                                                          '归属地'], db=db)
        self._lable = '歌手'
        self._db_table = 'singer'
        self._table_id = 'singer_id'

    def add(self):
        value = self._get_add_date()
        singer_num_sql = 'select count(*) from singer'
        add_sql = 'insert into singer values(%(singer_id)s,%(singer_name)s,%(singer_sex)s,' \
                  '%(country)s,%(song_type)s,%(short_name)s,%(region)s)'
        try:
            result, singer_num = self.db.deal_sql(singer_num_sql)
            singer_id = singer_num[0][0] + 1 if singer_num[0] else None
            if singer_id:
                if self.db.add(add_sql, {'singer_id': singer_id, 'singer_name':value[0],
                                         'singer_sex': value[1], 'country': value[2],
                                         'song_type': value[3], 'short_name': value[4],
                                         'region': value[5]}):
                    insert_logging(self.db, str(value[0]), action='添加', remark=value[-1])
                    sg.popup(f'添加歌手:{value[0]}成功!', title='提示')
                else:
                    raise BaseException
            else:
                sg.popup('网络出错！', title='提示')
        except BaseException:
            sg.popup('添加失败！', title='提示')
        finally:
            super().add()

    def _get_add_date(self):
        text = sg.popup_get_text('请输入歌手名,歌手性别,歌手所属国,类型,简写,归属地,修改原因(数据之间用,隔开)：')
        return re.split(r'[,，]', text if text is not None else '')

    def change(self):
        values = self._change_input()
        update_sql = 'update singer set s_name=%(singer_name)s,s_sex=%(singer_sex)s,' \
                     'country=%(country)s,songer_type=%(singer_type)s,pinyin_abbr=%(short_name)s,' \
                     'region=%(region)s where singer_id=%(singer_id)s'
        try:
            source_data = self._data[self.index]
            if self.db.change(update_sql, {'singer_name': self._return_right(values[0], source_data[1]),
                                           'singer_sex': self._return_right(values[1], source_data[2]),
                                           'country': self._return_right(values[2], source_data[3]),
                                           'singer_type': self._return_right(values[3], source_data[4]),
                                           'short_name': self._return_right(values[4], source_data[5]),
                                           'region': self._return_right(values[5], source_data[6]),
                                           'singer_id': source_data[0]}):
                insert_logging(self.db, str(values[0]), action='修改', remark=values[-1])
                sg.popup(f'歌手:{values[0]}(原名:{source_data[1]}修改成功！)', title='提示')
            else:
                sg.popup('修改失败！', title='提示')
        except TypeError:
            sg.popup('未选择歌手！', title='提示')
        finally:
            super().change()

    def _change_input(self):
        singer_name = sg.popup_get_text('请输入要修改的歌手名(无输入为不修改)：')
        singer_sex = sg.popup_get_text('请输入要修改的歌手性别(无输入为不修改)：')
        country = sg.popup_get_text('请输入要修改的歌手所属国(无输入为不修改)：')
        singer_type = sg.popup_get_text('请输入要修改的歌手所属国(无输入为不修改)：')
        short_name = sg.popup_get_text('请输入要修改的歌手简写(无输入为不修改)：')
        region = sg.popup_get_text('请输入要修改的歌手归属地(无输入为不修改)：')
        remark = sg.popup_get_text('请输入修改理由：')
        return [singer_name, singer_sex, country, singer_type, short_name, region, remark]


def main_m_ui(db):
    try:
        user = User(db, _get_data(db, 'ktv_user'))
        song = Song(db, _get_data(db, 'song'))
        singer = Singer(db, _get_data(db, 'singer'))
        button_event = {'': lambda: None,
                        '增加': user.add,
                        '删除': user.delete,
                        '修改': user.change,
                        '查找': user.find,
                        '增加0': song.add,
                        '删除1': song.delete,
                        '修改2': song.change,
                        '查找3': song.find,
                        '增加4': singer.add,
                        '删除5': singer.delete,
                        '修改6': singer.change,
                        '查找7': singer.find}
        # 组件
        user_frame = user.get_frame()
        song_frame = song.get_frame()
        singer_frame = singer.get_frame()
        # 布局
        layout = [[user_frame, song_frame, singer_frame]]
        window = sg.Window('管理员系统', layout)

        while True:

            event, values = window.read()
            # print(event)
            # print(values)
            if event is None:
                break
            user.update_index(values[0][0] if values[0] else None)
            song.update_index(values[1][0] if values[1] else None)
            singer.update_index(values[2][0] if values[2] else None)

            button_event[event]()
            window.refresh()
        window.close()
    except BaseException:
        sg.popup('网络出错！', title='提示')
        # print('出错')


def _get_data(db, key) -> list:
    result, data = db.deal_sql(f'select * from {key}')
    if not result:
        raise ConnectionError
    return [list(i) for i in data]


if __name__ == '__main__':
    from db import DBMethod

    dbase = DBMethod(user='root', password='123456', db='ktv_song')

    main_m_ui(dbase)
