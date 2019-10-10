import random


class Creat(object):
    def __init__(self, max_num, formula_num):
        self.max_num = max_num  # 最大范围
        self.formula_num = formula_num  # 公式最大条数
        self.level = random.randint(2, 4)  # 递归层数
        self.start_level = 0  # 递归开始层
        self.first_level = random.randint(1, self.level - 1)  # 第一个子式递归次数
        self.second_level = self.level - self.first_level  # 第二个子式递归次数
        self.operator = {
            1: '+',
            2: '-',
            3: '*',
            4: '÷',
        }

    def creator(self):
        math_op = '{}{}{}{}{}'.format(
            self.__creat_math_op(self.first_level),  # 随机数
            ' ',
            self.operator[random.randint(1, 4)],  # 随机选取运算符
            ' ',
            self.__creat_math_op(self.second_level),  # 'xx +|-|*|/ xx'
        )
        return math_op

    def __creat_math_op(self, level_chiose):
        random_num = random.randint(0, 1)
        self.start_level += 1
        if self.start_level == level_chiose:
            self.start_level = 0
            return random.randint(0, self.max_num)
        math_op = '{}{}{}{}{}{}{}'.format(
            self.__brackets(random_num, 0),  # '('
            random.randint(0, self.max_num),  # 随机数
            ' ',
            self.operator[random.randint(1, 4)],  # 随机选取运算符
            ' ',
            self.__creat_math_op(level_chiose),  # 'xx +|-|*|/ xx'
            self.__brackets(random_num, 1),  # ')'
        )
        self.start_level = 0
        return math_op

    def __brackets(self, random_num, chiose):  # 决定括号是否填入
        if random_num:
            if chiose:
                return ')'
            else:
                return '('
        return ''

    def creat_more(self):  # 迭代器
        op_num = 1
        while True:
            math_op = self.creator()
            if self.__check_math_op(math_op):
                yield math_op
                op_num += 1
                self.__init_variable()

    def __init_variable(self):  # 初始化以下值
        self.start_level = 0
        self.level = random.randint(2, 4)
        self.first_level = random.randint(1, self.level - 1)
        self.second_level = self.level - self.first_level

    def __check_math_op(self, math_op):  # 检测数学表达式的合法性和处理假分数
        pass

    def __repr__(self):
        return f'Creat(max_num={self.max_num}, formula_num={self.formula_num})'


if __name__ == '__main__':
    t = Creat(50, 10)
    for i in t.creat_more():
        print(i)