import time

class Record:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __get__(self, instance, owner):
        localtime = time.asctime(time.localtime(time.time()))
        f = open('record.txt','a')
        ass = str(self.b + '变量于北京时间' + localtime + '被读取， '+ self.b + '=' + str(self.a))
        f.write(ass+'\n')
        f.close
        return self.a
    def __set__(self, instance, value):
        self.a = value
        localtime = time.asctime(time.localtime(time.time()))
        f = open('record.txt','a')
        can = str(self.b + '变量于北京时间' + localtime + '被修改，' + self.b+ '=' + str(self.a))
        f.write(can+'\n')
        f.close

class Test:
    x = Record(10, 'x')
    y = Record(8.8, 'y')
        
    
