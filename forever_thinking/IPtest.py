from attr import attrs, attrib


def check_num(instance, attribute, value):
    if type(value) == int and value > 10:
        raise ValueError(f'{value}大于10！')
    elif type(value) != Test_:
        raise TypeError(f'{attribute}不是Test_')


@attrs
class Test(object):
    a = attrib()
    b = attrib(validator=check_num)
    headers = attrib(default={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                            'AppleWebKit/537.36 (KHTML, like Gecko) '
                                            'Chrome/74.0.3729.169 Safari/537.36'})

    def play(self):
        print(self.a, self.b)

@attrs
class Test_(object):
    a = attrib()
    b = attrib()


    def play(self):
        print(self.a, self.b)


t_ = Test_(3, 1)
t = Test(3, t_)
print(type(t.headers))




