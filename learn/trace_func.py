import functools  # 用于查看被装饰的函数的元数据和文档数据


def trace_func(func):
    @functools.wraps(func)  # 此处能将被装饰函数的元数据复制到装饰器闭包中，方便调试被装饰函数
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


'''@trace_func
def ttee(a: list):
    """asd"""
    return [i for i in a if i != None]

if __name__ == '__main__':
    print(ttee.__name__)
    print(ttee.__doc__)'''