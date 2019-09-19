def outer(new):
    def inner(num):
        print('函数开始！')
        new(num)
        print('函数结束')
    return inner


@outer   # 闭包
def foo(num):
    print(num)


foo(2)
