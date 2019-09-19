import socket
import threading


def send_(c):
    while 1:
        new_ = input('请输入：')
        if new_ == '0':
            c.close()
            break
        c.send(bytes(new_, encoding='utf-8'))


def get_(c):
    while 1:

        print(c.recv(1024).decode())

def listen_(addr):
    print('欢迎' + str(addr) + '连接！！')
    t1 = threading.Thread(target=send_, args=(c,), name='t1')
    t2 = threading.Thread(target=get_, args=(c,), name='t2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()

s = socket.socket()
host = '192.168.1.232'
port = 21
s.bind((host, port))
while 1:
    print(1)
    s.listen(5)
    c, addr = s.accept()
    threading.Thread(target=listen_, args=(addr,), name='t').start()


