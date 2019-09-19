import socket
import os
from attr import attrib, attrs
import json


@attrs
class FtpClient(object):
    log = attrib(type=int, default=0)
    con = attrib(type=int, default=0)
    msg_dic = attrib(default=None)
    host = attrib(type=str, default='192.168.1.232', kw_only=True)  # 主机号
    command_port = attrib(type=int, default=21, kw_only=True)  # 端口号（命令端口号）
    data_port = attrib(type=int, default=20, kw_only=True)  # 端口号（命令端口号）
    command_s = attrib(init=False, default=socket.socket())
    data_s = attrib(init=False, default=socket.socket())
    p_size = attrib(init=False, default=1024)  # 先固定分片


    def link_(self):
        self.command_s.connect((self.host, self.command_port))
        print(self.command_s.recv(1024).decode())
        while 1:
            self.deal_command()

    def deal_command(self):
        final_data = None
        command = None
        data = None
        if self.log:
            source_data = str(input('FTP/User>')).strip()
            while 'pass' in source_data or 'user' in source_data:
                print('502： 命令未实现')
                source_data = str(input('FTP/User>')).strip()
            else:
                if ' ' in source_data:
                    command, data = source_data.split(' ', 1)
                    final_data = '{0} {1}'.format(command.lower(), data)
                else:
                    final_data = source_data.lower()
                    command = final_data
        else:
            source_data = str(input('FTP>')).strip()
            if ' ' in source_data:
                command, data = source_data.split(' ', 1)
                final_data = '{0} {1}'.format(command.lower(), data)
            else:
                final_data = source_data.lower()
                command = final_data
        self.deal_func(command.lower(), final_data, data)

    def deal_func(self, cmd, final_data, data):
        if hasattr(self, 'cmd_%s' % cmd):
            func = getattr(self, 'cmd_%s' % cmd)
            if cmd == 'get' or cmd == 'put':
                func(final_data, data)
            else:
                func(final_data)
        else:
            self.command_s.send(bytes(final_data, encoding='utf-8'))

    def cmd_user(self, final_data):
        self.command_s.send(bytes(final_data, encoding='utf-8'))
        data_message = self.command_s.recv(1024).decode()
        print(data_message)

    def cmd_pass(self, final_data):
        self.command_s.send(bytes(final_data, encoding='utf-8'))
        data_message = self.command_s.recv(1024).decode()
        print(data_message)
        if '230' in data_message:
            self.log = 1

    def cmd_get(self, final_data, data):
        if self.log:
            if self.con == 0:
                print('ye')
                self.data_s.connect((self.host, self.data_port))
                self.con = 1
            sour_data = self.__send_data_command(final_data)
            while '502' in sour_data:
                source_data = str(input('FTP/User>')).strip()
                while 'pass' in source_data or 'user' in source_data:
                    print('502： 命令未实现')
                    source_data = str(input('FTP/User>')).strip()
                else:
                    if ' ' in source_data:
                        command, data = source_data.split(' ', 1)
                        final_data = '{0} {1}'.format(command.lower(), data)
                sour_data = self.__send_data_command(final_data)
            else:
                self.msg_dic = json.loads(sour_data)
                self.command_s.send(bytes('OK', encoding='utf-8'))
            received_size = 0
            file_size = self.msg_dic['size']
            file_name = self.msg_dic['filename']
            with open(r'C:\Users\10248\Desktop\%s' % file_name, 'wb') as f:  #
                while received_size < file_size:
                    data = self.data_s.recv(1024)
                    f.write(data)
                    received_size += len(data)
                else:
                    print('文件[%s]传输完成..' % file_name)  # 文件传输完成
        else:
            print(self.command_s.recv(1024).decode())

    def cmd_put(self, final_data, file_name):  # 用d端口
        if self.con == 0:
            self.data_s.connect((self.host, self.data_port))
            self.con = 1
        self.command_s.send(bytes(final_data, encoding='utf-8'))
        if self.log:
            try:
                if os.path.isfile(file_name):
                    filesize = os.stat(file_name).st_size  # 获取文件大小
                    msg_dic = {'action': 'put', 'filename': file_name.replace(os.path.dirname(file_name), ''), 'size': filesize}
                    self.data_s.send(bytes(json.dumps(msg_dic).encode('utf-8')))
                    print(self.data_s.recv(self.p_size).decode())
                    with open(r'%s' % file_name, 'rb') as f:
                        for i in f:
                            self.data_s.send(i)
                        else:
                            print('文件上传完毕')
                            print(self.command_s.recv(1024).decode())
                else:
                    print('无该文件')
            except:
                pass
        else:
            self.command_s.recv(1024).decode()

    def cmd_dir(self, final_data):
        if self.con == 0:
            self.data_s.connect((self.host, self.data_port))
            self.con = 1
        print('root')
        self.command_s.send(bytes(final_data, encoding='utf-8'))
        finally_file = self.data_s.recv(1024).decode()
        if '502' not in finally_file:
            print(finally_file)
            while 1:
                data = self.data_s.recv(1024).decode()
                print(data)
                if not data:
                    self.data_s.close()
                    self.data_s.__init__()
                    self.con = 0
                    break
        else:
            print(self.command_s.recv(1024).decode())

    def get_request(self):  # 用命令端口
        data_message = self.command_s.recv(1024).decode()
        print(data_message)
        if '230' in data_message:
            self.log = 1

    def __send_data_command(self, final_data):  # 用d端口
        self.command_s.send(bytes(final_data, encoding='utf-8'))
        sour_data = self.command_s.recv(1024).decode()
        print(sour_data)
        return sour_data


if __name__ == '__main__':
    fclinet = FtpClient()
    fclinet.link_()
