import random as r
class Wugui:
    def __init__(self):
        self.a = 1
        self.x1 = r.randint(0,10)
        self.y1 = r.randint(0,10)
        print('乌龟的位置在：(%d,%d)' % (self.x1,self.y1))
    def move(self):
        s = r.randint(1,2)
        if s == 1:
            if self.x1 == 10:
                self.a = 0
                print('乌龟死亡')
            elif self.x1 == 0:
                self.a = 0
                print('乌龟死亡')
            else:
                self.a = 1
                self.x1 += 1
                    
        else:
            if self.y1 == 10:
                self.a = 0
                print('乌龟死亡')
            elif self.y1 == 0:
                self.a= 0
                print('乌龟死亡')
            else:
                self.a = 1
                self.y1 += 1
        print('乌龟的新位置在：(%d,%d)' % (self.x1,self.y1))
class Fish:
    def __init__(self):
        self.k = 1
        self.x2 = r.randint(0,10)
        self.y2 = r.randint(0,10)
        print('鱼儿的位置在：(%d,%d)' % (self.x2,self.y2))
    def move(self):
        s = r.randint(1,2)
        if s == 1:
            if self.x2 == 10:
                self.k = 0
                print('鱼儿死亡')
            elif self.x2 == 0:
                self.k = 0
                print('鱼儿死亡')
            else:
                self.k = 1
                self.x2 += 1
                        
        else:
            if self.y2 == 10:
                self.k = 0
                print('鱼儿死亡')
            elif self.y2 == 0:
                self.k = 0
                print('鱼儿死亡')
            else:
                self.k = 1
                self.y2 += 1
        print('鱼儿的新位置在：(%d,%d)' % (self.x2,self.y2))
class Game:
    def __init__(self):
        self.w = Wugui()
        self.f = Fish()
    def move(self):
        while 1:
            if self.w.a == 0:
                print('鱼儿胜利')
                break
            elif self.f.k == 0:
                print('乌龟胜利')
                break
            self.w.move()
            self.f.move()
g = Game()
g.move()
    
        
        
        
    
        
            
