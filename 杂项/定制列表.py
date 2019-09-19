class CountList:
    def __init__(self,*args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)), 0)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        self.key = key
        self.count[self.key] += 1
        return self.values[self.key]

    #设置一个元素的行为
    def __setitem__(self, key, value):
        self.values[self.key] = value
        return self.values[self.key]

    #删除一个元素的行为
    def __delitem__(self, key):
        del self.values[self.key]
        self.count[self.key] -= 1
        return self.count[self.key]

    #增加counter(index)方法，返回index参数所指定的元素记录的访问次数
    def counter(self,index):
        self.key = index
        return self.count[self.key]
        
