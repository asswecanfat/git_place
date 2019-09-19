#先写闰年的类
class LeapYear:
    def __init__(self):
        self.a = 2018
        self.b = 0
#__iter__返回迭代器自身
    def __iter__(self):
        return self
    
#再写计算闰年的方法
    def __next__(self):
        while (self.a % 4 == 0 and self.a % 100 != 0) or (self.a % 400 == 0):
            self.a -= 1
            return self.a + 1

           



            

            
        
    
