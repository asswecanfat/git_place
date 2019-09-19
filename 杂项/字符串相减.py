class Nstr(str):
    def __init__(self,a):
        self.a = list(a)
    def __sub__(self,other):
        for index in self.a:
            for ind in other.a:
                if index == ind:
                    self.a.remove(index)
        ass = ''.join(self.a)
        print(ass)
	    
