import pickle
import os

class MyDes:
    def __init__(self, a):
        self.a = a + '.pkl'
        self.b = a
        
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value
        f = open('test.py', 'a')
        f.write(self.b + '\n')
        f.close()
        pickle_file = open(self.a, 'wb')
        pickle.dump(self.value, pickle_file)
        pickle_file.close()
        return self.value

    def __delete__(self,instance):
        os.remove(self.a)

class Test:
    x = MyDes('x')
    y = MyDes('y')
    

        
