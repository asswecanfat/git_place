class C():
    def __init__(self, *a):
        self.a = [*a]
        if len(self.a) == 0:
            print('并没有传入参数~')
        else:
            print('传入了%d个参数，为：' % len(self.a), end = '')
            for each in self.a:
                print(each,end=' ')
                        
