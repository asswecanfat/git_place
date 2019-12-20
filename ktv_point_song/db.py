import pymysql
from datetime import datetime
import re


class DBMethod(object):
    def __init__(self,
                 host='127.0.0.1',
                 port=3306,
                 **kwargs
                 ):
        self._host = host
        self._port = port
        self._kwargs = kwargs
        self._target = None  # 查询目标
        self._index = {'singer': 'singer.s_name',
                       'song': 'song.so_name',
                       'singer_py': 'singer.pinyin_abbr',
                       'song_py': 'song.song_py'}
        try:
            self._connect = pymysql.connect(host=self._host,
                                            port=self._port,
                                            user=self._kwargs['user'],
                                            password=self._kwargs['password'],
                                            db=self._kwargs['db'],
                                            charset='utf8', )
            self._cursor = self._connect.cursor()
        except ConnectionError:
            print('连接出错')

    def __enter__(self):
        return self

    # 增<--(管理员，VIP)
    def add_user(self, user_name, u_password, real_name, u_sex):
        num_sql = 'select count(*) from ktv_user'
        try:
            self._cursor.execute(num_sql)
            user_id = f'{301 + self._cursor.fetchall()[0][0]}'
            time = re.sub(r'\.\d+', '', str(datetime.today()))
            result = self._cursor.execute('insert into ktv_user values(%(user_id)s,'
                                          '%(user_name)s,'
                                          '%(u_password)s,'
                                          '%(real_name)s,'
                                          '%(u_sex)s,'
                                          '%(time)s)', {'user_id': user_id,
                                                        'user_name': user_name,
                                                        'u_password': u_password,
                                                        'real_name': real_name,
                                                        'u_sex': u_sex,
                                                        'time': time})
            self._connect.commit()
        except:
            # 出错就回滚
            result = False
            self._connect.rollback()
        return result

    # 删<--(管理员，顾客删除收藏)
    def delete_data(self):
        try:

            self._connect.commit()
        except:
            self._connect.rollback()

    # 改<--管理员
    def change_data(self):
        try:

            self._connect.commit()
        except:
            self._connect.rollback()

    def update_rank(self, in_son):
        sql = f'update rank_list set click=click+1 where son_name=%(sname)s'
        try:
            self._cursor.execute(sql, {'sname': in_son})
            self._connect.commit()
        except:
            self._connect.rollback()

    # 查<--所有人
    def _find_data(self, arg):
        sql = 'select so_name,song_length from song,singer where song.singer_i=singer.singer_id and ' \
              f'{self._target}=%(pin)s'
        self._cursor.execute(sql, {'pin': arg})
        return self._cursor.fetchall()

    def find_data_by(self, what, arg):
        self._target = self._index[what]
        return self._find_data(arg)

    def get_rank_data(self):
        sql = 'select son_name,sin_name,click from rank_list order by click DESC'
        self._cursor.execute(sql)
        return self._cursor.fetchall()

    def deal_sql(self, sql):
        result = self._cursor.execute(sql)
        data = self._cursor.fetchall()
        return result, data

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._cursor.close()
        self._connect.close()

    def close(self):
        self._cursor.close()
        self._connect.close()

    def __repr__(self):
        return f'DBMethod(host="127.0.0.1", port=3306, **kwargs->{self._kwargs!r})'


if __name__ == '__main__':
    with DBMethod(user='root', password='123456', db='ktv_song') as db:
        pass
