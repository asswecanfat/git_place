import threading
import socket
from attr import attrs, attrib
import os
import pickle
import json


@attrs
class FtpSever(object):
    user_data = attrib(default=None)  # 用户信息
    flie_path = attrib(default=r'D:\wps\ftp_root')  # 服务器的目录
    dir_count = attrib(default=0)
    file_count = attrib(default=0)
    con = attrib(type=int, default=0)
    data_s = attrib(init=False, default=socket.socket())
    p_size = attrib(init=False, default=1024)  # 固定分片长度
    log = attrib(type=int, default=0)  # 登录状态
    account = attrib(type=int, default=0)  # 账号验证状态（0为没有输入，1为输入正确，-1为输入错误）
    password = attrib(type=int, default=0)  # 密码验证状态（0为没有输入，1为输入正确，-1为输入错误）
    d = attrib(default=None)  # 数据socket，None为未开启
    c = attrib(default=None)  # 命令socket， None为未接收
    data_port = attrib(type=int, default=20, kw_only=True)  # 数据端口
    host = attrib(type=str, default='192.168.43.221', kw_only=True)  # 主机号()192.168.1.232

    @staticmethod
    def first_send(c):  # 类的静态方法
        c.send(bytes('欢迎进入FTP服务器！', encoding='utf-8'))

    def main_act(self, c):  # 主要行动
        self.c = c
        FtpSever.first_send(self.c)
        self.load_user_data()
        while 1:
            if self.log == 1 and self.con == 0:
                self.data_s.bind((self.host, self.data_port))
                self.data_s.listen(1)
                self.d, addr = self.data_s.accept()
                self.con = 1
            self.deal_command()

    def deal_command(self):  # 命令处理
        data = self.c.recv(1024).decode()
        print(data)
        if not self.log:
            if ' ' in data:
                cmd, argv = data.split(' ', 1)
            else:
                cmd, argv = data, None
        else:
            if ' ' in data:
                cmd, argv = data.split(' ', 1)
            else:
                cmd, argv = data, None
        self.deal_func(cmd, argv)

    def deal_func(self, cmd, argv):  # 命令处理方法（反射）
        if hasattr(self, 'cmd_%s' % cmd):  # 客户端输入的命令反射到服务器的方法
            func = getattr(self, 'cmd_%s' % cmd)
            if cmd == 'dir' or cmd == 'put':
                func()
            else:
                func(argv)
        else:
            self.c.send(bytes('502:命令未实现', encoding='utf-8'))  # 发送错误代码

    def load_user_data(self):  # 读取根目录下的user_data.pkl文件中的字典
        with open(r'D:\wps\ftp_root\user_data.pkl', 'rb') as f:
            data = pickle.load(f)  # 用户的账号密码以字典类存在腌菜中
            self.user_data = data

    def cmd_user(self, account):  # 账号指令
        if not self.log:
            if account is not None:
                self.account = -1
                for g in self.user_data.keys():
                    if str(g) == str(account):
                        self.account = 1
                        break
            self.c.send(bytes('200:命令成功', encoding='utf-8'))  # 发送响应代码
        else:
            self.c.send(bytes('502:命令未实现', encoding='utf-8'))  # 发送错误代码

    def cmd_pass(self, password):  # 密码指令
        if not self.log:
            if password is not None:
                if self.account == 0:
                    if str(password) == 'admin':
                        self.password = 1
                        self.c.send(bytes('200:命令成功\r\n230:登陆成功', encoding='utf-8'))  # 发送响应代码
                        self.log = 1
                    else:
                        self.c.send(bytes('200:命令成功\r\n530:登陆失败', encoding='utf-8'))  # 发送响应代码
                else:
                    self.password = -1
                    for g in self.user_data.values():
                        if str(g) == str(password):
                            self.password = 1
                            break
                    if self.password == 1 and self.account == 1:
                        self.c.send(bytes('200:命令成功\r\n230:登陆成功', encoding='utf-8'))  # 发送响应代码
                        self.log = 1
                    else:
                        self.c.send(bytes('200:命令成功\r\n530:登陆失败', encoding='utf-8'))  # 发送响应代码
        else:
            self.c.send(bytes('502:命令未实现', encoding='utf-8'))  # 发送错误代码

    def cmd_get(self, file_name):  # 上传（用户下载指令）
        if self.log:
            try:
                file_data = r'{}\\{}'.format(self.flie_path, file_name)
                if os.path.isfile(file_data):
                    filesize = os.stat(file_data).st_size  # 获取文件大小
                    msg_dic = {'action': 'put', 'filename': file_name, 'size': filesize}
                    self.c.send(bytes(json.dumps(msg_dic).encode('utf-8')))
                    self.c.recv(self.p_size).decode()
                    with open(r'%s' % file_data, 'rb') as f:
                        for g in f:
                            self.d.send(g)
                        else:
                            print('文件传输完毕')
                else:
                    self.c.send(bytes('502:命令未实现\r\n无该文件', encoding='utf-8'))
            except:
                self.c.send(bytes('502:命令未实现\r\n无该文件', encoding='utf-8'))
        else:
            self.c.send(bytes('502:命令未实现', encoding='utf-8'))  # 发送错误代码

    def cmd_put(self):  # 下载（用户上传）, 使用d端口，用户上传指令
        if self.log:
            sour_data = self.d.recv(1024).decode()
            msg_dic = json.loads(sour_data)
            self.d.send(bytes('OK', encoding='utf-8'))
            received_size = 0
            file_size = msg_dic['size']
            file_name = msg_dic['filename']
            with open(r'D:\wps\ftp_root\%s' % file_name, 'wb') as f:  #
                while received_size < file_size:
                    data = self.d.recv(1024)
                    f.write(data)
                    received_size += len(data)
                else:
                    self.c.send(bytes('[FtpServer]文件上传成功', encoding='utf-8'))  # 发送响应代码
        else:
            self.c.send(bytes('502:命令未实现', encoding='utf-8'))  # 发送错误代码

    def cmd_dir(self):  # dir指令
        if self.log:
            self.get_all_dir()
            self.d.close()
            self.data_s.close()
            self.data_s.__init__()
            self.con = 0
            self.dir_count = 0
            self.file_count = 0
        else:
            self.c.send(bytes('502:命令未实现', encoding='utf-8'))

    def get_all_dir(self, sp="|"):  # 发送文件夹结构
        # 得到当前目录下所有的文件
        fills_list = os.listdir(self.flie_path)
        sp += "-"
        # 处理每一个文件
        for file_name in fills_list:
            # 判断是否是路径（用绝对路径）
            file_abs_path = os.path.join(self.flie_path, file_name)
            if os.path.isdir(file_abs_path):
                self.dir_count += 1
                self.d.send(bytes('{}{}{}'.format(sp, "目录：", file_name), encoding='utf-8'))
                self.get_all_dir(file_abs_path)
            else:
                self.file_count += 1
                self.d.send(bytes('{}{}{}'.format(sp, "普通文件：", file_name), encoding='utf-8'))

    @staticmethod
    def register():  # 服务器端注册
        while 1:
            print('创建用户~~~')
            account = input('请输入账号:')
            password = input('请输入密码:')
            with open(r'D:\wps\ftp_root\user_data.pkl', 'rb') as f:
                data = pickle.load(f)  # 用户的账号密码以字典类存在腌菜中
            with open(r'D:\wps\ftp_root\user_data.pkl', 'wb') as g:
                data[account] = password
                pickle.dump(data, g)
            print('创建成功~~~')


@attrs
class RunFtpServer(object):
    command_s = attrib(init=False, default=socket.socket())
    command_port = attrib(type=int, default=21, kw_only=True)  # 命令端口号
    host = attrib(type=str, default='192.168.43.221', kw_only=True)  # 主机号()192.168.43.221

    def keep_listen_then_active(self):
        self.command_s.bind((self.host, self.command_port))  # 绑定ip
        # 开始监听
        self.command_s.listen(5)
        while 1:
            c, addr = self.command_s.accept()  # c为连接后返回的新的套接字对象，addr为返回的连接的ip
            threading.Thread(target=FtpSever().main_act, args=(c,), name='main', daemon=True).start()


if __name__ == '__main__':
    ftps = RunFtpServer()
    t1 = threading.Thread(target=ftps.keep_listen_then_active, args=())
    t2 = threading.Thread(target=FtpSever.register, args=(), daemon=True)  # FTPServer类的静态注册方法，为守护线程
    a = [t1, t2]
    for i in a:
        i.start()
    for o in a:
        o.join()
