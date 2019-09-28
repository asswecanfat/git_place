

class HotDog(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'HotDog({self.name!r})'

    @classmethod  # 可用于生成工厂模式
    def name_fuck(cls):
        return cls('fuck')

    @classmethod
    def name_dick(cls):
        return cls('dick')


if __name__ == '__main__':
    h = HotDog('ass')
    print(h)
    print(h.name_dick())
    print(h.name_fuck())
    print(HotDog.name_fuck())
    print(HotDog.name_dick())