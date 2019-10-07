

class Ans:
    def __init__(self, name):
        self.name = name

    def __iter__(self):
        return Ansor(self)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name})'

class Ansor:
    def __init__(self, source):
        self.source = source

    def __next__(self):
        return self.source.name

class Acount_list(object):
    def __init__(self, num_list):
        self.num_list = num_list
        self.count = 0
        self._len = len(num_list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self._len:
            raise StopIteration
        else:
            num = self.num_list[self.count]
            self.count += 1
            return num


def _for(all):
    for i in all:
        yield i



if __name__ == '__main__':
    a = Acount_list([1,2,3])
    '''for i in a:
        print(i)'''
    ass = _for('1000')
    for i in ass:
        print(i)
