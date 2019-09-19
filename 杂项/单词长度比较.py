class Word(str):
    def __init__(self,a=''):
        ass = list(a)
        self.a = len(a)
        i = 0
        for each in ass:
            if each != ' ':
                i += 1
            else:
                self.a = i
                print(self.a)
                break
                                    
    def __lt__(self,other):
        return self.a < other.a
    def __le__(self,other):
        return self.a <= other.a
    def __eq__(self,other):
        return self.a == other.a
    def __ne__(self,other):
        return self.a != other.a
    def __gt__(self,other):
        return self.a > other.a
    def __ge__(self,other):
        return self.a >= other.a
    
