from attr import attrib, attrs
import random
import sys


def trans_num(value):
    return int(value)


@attrs
class TwoScoreFind(object):
    # 基于数组的
    low = attrib(default=None)
    high = attrib(default=None)
    mid = attrib(default=None)
    need_sort_list = attrib(kw_only=True, type=list, default=[i for i in range(0, 20)])
    find_num = attrib(kw_only=True, type=int, default=random.randint(0, 100), converter=trans_num)


    def init_keyword(self):
        self.low = 0
        self.high = len(self.need_sort_list) - 1
        self.mid = (self.low + self.high) // 2

    def start(self):
        if self.low > self.high:
            return None
        if self.find_num == self.need_sort_list[self.mid]:
            return self.mid
        elif self.find_num > self.need_sort_list[self.mid]:
            self.low = self.mid + 1
            self.mid = (self.low + self.high) // 2
            return self.start()
        elif self.find_num < self.need_sort_list[self.mid]:
            self.high = self.mid - 1
            self.mid = (self.low + self.high) // 2
            return self.start()

    def re_init_keyword(self):  # 用于循环当中
        self.low.__init__()
        self.high.__init__()
        self.mid.__init__()

    @staticmethod
    def random_num(r_num):
        _ = random.sample(range(0, 1000000), r_num)
        _.sort()
        return _  # 暂时使用自带的排序


if __name__ == '__main__':
    print('欢迎使用查找数字功能！')
    print('1.生成随机列表')
    print('2.查找数字')
    print('3.退出')
    need_sort_list = None
    while 1:
        try:
            choose = int(input('请输入功能：'))
            if choose == 1:
                x = int(input('请输入随机列表规模（即为多长）：'))
                need_sort_list = TwoScoreFind.random_num(x)
                print('{}{}'.format('随机生成的列表为：', need_sort_list))
            elif choose == 2:
                if need_sort_list is not None:
                    print('{}{}'.format('随机生成的列表为：', need_sort_list))
                    find_num = int(input('请输入要查找的数字：'))
                    tcf = TwoScoreFind(find_num=find_num, need_sort_list=need_sort_list)
                    tcf.init_keyword()
                    check = tcf.start()
                    if check:
                        print('{}{}'.format('位置在：', check + 1))
                    else:
                        print('不存在该数字')
                else:
                    print('{}{}'.format('使用默认列表为：', TwoScoreFind().need_sort_list))
                    find_num = int(input('请输入要查找的数字：'))
                    tcf = TwoScoreFind(find_num=find_num)
                    tcf.init_keyword()
                    check = tcf.start()
                    if check:
                        print('{}{}'.format('位置在：', check + 1))
                    else:
                        print('不存在该数字')
            elif choose == 3:
                print('已退出！！')
                sys.exit()
            else:
                print('不存在此功能')
        except TypeError as result:
            print('输入的应该为数字！！请重新输入！！')
            print(result)
