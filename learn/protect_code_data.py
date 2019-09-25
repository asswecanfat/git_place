"""
模板字符串可以有效的保护代码的隐私数据

"""

from string import Template


class ToTest(object):
    def __init__(self):
        pass


def _test1(user_input=None):
    t = Template('你好啊，$name朋友！')
    print(t.substitute(name='Van'))
    if user_input is not None:
        print(Template(user_input).substitute(t=to_test))


def _test2(user_input=None):
    if user_input is not None:
        print(user_input.format(t=to_test))


if __name__ == '__main__':
    SECRET = 110
    _test1()
    to_test = ToTest()
    user_input2 = '{t.__init__.__globals__[SECRET]}'
    user_input1 = '${t.__init__.__globals__[SECRET]}'
    _test2(user_input2)  # 此时可能暴露数据
    try:
        _test1(user_input1)
    except ValueError:
        print('成功保护了全局数据')