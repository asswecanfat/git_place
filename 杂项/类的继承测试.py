class A():
    def __init__(self):
        print("进入A…")
        print("离开A…")

class B(A):
    def __init__(self):
        print("进入B…")
        A.__init__(self)
        print("离开B…")
            
class C(A):
    def __init__(self):
        print("进入C…")
        A.__init__(self)
        print("离开C…")

class D(B, C):
    def __init__(self):
        print("进入D…")
        B.__init__(self)
        C.__init__(self)
        print("离开D…")
