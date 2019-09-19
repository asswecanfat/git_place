class Duck1():
    def duck(self):
        print("这是Duck1")

class Duck2():
    def duck(self):
        print("这是Duck2")

class User():
    def test1(self, duck):
        duck.duck(self)
    def test2(self, duck):
        duck.duck(self)
a = User()
a.test1(Duck1)

