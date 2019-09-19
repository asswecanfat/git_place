class Nstr(str):
    def __init__(self,x):
        self.x = list(x)
        
    def __add__(self,other):
        ass = 0
        other.x = list(other)
        for inde in self.x:
            ass += ord(inde)
        for iNd in other.x:
            ass += ord(iNd)
        return ass
    def __sub__(self,other):
        skr = 0
        can = 0
        other.x = list(other)
        for inde in self.x:
            skr += ord(inde)
        for iNd in other.x:
            can += ord(iNd)
        return (skr - can)
    def __mul__(self,other):
        new = 0
        aSs = 0
        other.x = list(other)
        for index in self.x:
            new += ord(index)
        for ind in other.x:
            aSs += ord(ind)
        return (new * aSs)
    def __truediv__(self,other):
        sKr = 0
        cAn = 0
        other.x = list(other)
        for inde in self.x:
            sKr += ord(inde)
        for iNd in other.x:
            cAn += ord(iNd)
        return (sKr / cAn)
    def __floordiv__(self,other):
        sKR = 0
        cAN = 0
        other.x = list(other)
        for inde in self.x:
            sKR += ord(inde)
        for iNd in other.x:
            cAN += ord(iNd)
        return (sKR // cAN)
        
