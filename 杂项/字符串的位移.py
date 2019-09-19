class Nstr():
    def __init__(self,a):
        self.a = list(a)
        
    def __lshift__(self,other):
        self.a = self.a[other:]+self.a[0:other]
        self.a = ''.join(self.a)
        return self.a
    def __rshift__(self,other):
        self.a = self.a[-(other):] + self.a[0:-(other)]
        self.a = ''.join(self.a)
        return self.a
