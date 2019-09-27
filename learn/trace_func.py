

def trace_func(func):
    def _fuck(*args, **kwargs):
        print(f'开始跟踪：{func.__name__}()函数，'
              f'输入参数为：{args}, {kwargs}')
        real_data = func(*args, **kwargs)
        print(f'{func.__name__}()函数返回了：{real_data}')
        return real_data
    return _fuck
