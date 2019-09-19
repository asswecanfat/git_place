import socket
import threading
import os

s = socket.socket()
host = '192.168.1.232'
prot = 21
s.connect((host, prot))



def print_(s):
    while 1:
        print(s.recv(1024).decode())

def get_(s):
    while 1:
        back_ = input('请输入：')
        if back_ == '0':
            s.close()
            break
        s.send(bytes(back_, encoding='utf-8'))

t1 = threading.Thread(target=print_, args=(s,), name='t1')
t2 = threading.Thread(target=get_, args=(s,), name='t2')
t1.start()
t2.start()
t1.join()
t2.join()




