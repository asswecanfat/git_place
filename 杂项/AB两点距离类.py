import math as m

class Point:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def A(self):
        print('A点为（%d,%d）' % (self.x1,self.y1))
    def B(self):
        print('B点为（%d,%d）' % (self.x2,self.y2))

class Line(Point):
    def __init__(self,x1,y1,x2,y2):
        super().__init__(x1,y1,x2,y2)
    def getLen(self):
        len = float(abs(m.sqrt((self.x1-self.x2)**2+(self.y1-self.y2)**2)))
        print('A,B两点的距离为：%f' % len)

x1 = int(input('请输入A的x坐标:'))
y1 = int(input('请输入A的y坐标:'))
x2 = int(input('请输入B的x坐标:'))
y2 = int(input('请输入B的y坐标:'))
l = Line(x1,y1,x2,y2)
l.getLen()

        
    
        
    
