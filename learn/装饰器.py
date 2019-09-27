

def _1(func):
    def fuck():
        func()
        print(f'调用的方法为：{func.__name__}')
        return [i+j for i, j in range()]
    return fuck


@_1
def a():
    print('方法运行中')


if __name__ == '__main__':
    a()
