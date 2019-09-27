

def trace_func(func):
    def _fuck(*args, **kwargs):
        real_data = None
        print(f'开始跟踪：{func.__name__}()函数，'
              f'输入参数为：{args}, {kwargs}')
        try:
            real_data = func(*args, **kwargs)
        except TypeError:
            print(f'{func.__name__}()函数的参数输入有误！！')
        else:
            print(f'{func.__name__}()函数返回了：{real_data}')
        return real_data
    return _fuck


''''@trace_func
def ttee(a: list):
    return [i for i in a if i != None]

if __name__ == '__main__':
    ttee([1], [1])'''