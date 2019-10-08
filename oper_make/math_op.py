import random


class Creat(object):
    def __init__(self, max_num, formula_num):
        self.max_num = max_num  # 最大范围
        self.formula_num = formula_num  # 公式最大条数
        self.level = random.randint(2, 4)  # 递归层数
        self.start_level = 0  # 递归开始层
        self.operator = {
            1: '+',
            2: '-',
            3: '*',
            4: '/',
        }

    def creator(self):
        random_num = random.randint(0, 1)
        self.start_level += 1
        if self.start_level == self.level:
            return random.randint(0, self.max_num)
        math_op = '{}{}{}{}{}{}{}'.format(
            self.__brackets(random_num, 0),  # '('
            random.randint(0, self.max_num),  # 随机数
            ' ',
            self.operator[random.randint(1, 4)],  # 随机选取运算符
            ' ',
            self.creator(),  # 'xx +|-|*|/ xx'
            self.__brackets(random_num, 1),  # ')'
        )
        return math_op

    def __brackets(self, random_num, chiose):  # 决定括号是否填入
        if random_num:
            if chiose:
                return ')'
            else:
                return '('
        return ''

    def deal_math_op(self, math_op):  # 检测数学表达式的合法性和处理假分数
        pass

    def __repr__(self):
        return f'Creat(max_num={self.max_num}, formula_num={self.formula_num})'


if __name__ == '__main__':
    t = Creat(50, 10)
    print(t.creator())