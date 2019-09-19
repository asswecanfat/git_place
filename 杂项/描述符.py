class MyDes:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __get__(self, instance, owner):
        print('正在获取变量:x')
        return self.a
        
    def __set__(self, instance, value):
        print('正在修改变量:x')
        self.a = value
        
    def __delete__(self, instance):
        print('正在删除变量：x')
        print('噢~这个变量没法删除~')

class Test:
    x = MyDes(10, 'x')
        
        
