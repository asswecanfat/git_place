import random
from op_error import ExceptError, ReduceError
from math_op_analysis import AnalyOp
from num_creat import NumCreat
from wirte_file import write_in_file, deal_math_op
from data_sturct import DataSave
from learn.time_sum import TimeSum


class Creat(object):
    def __init__(self, max_num: int, formula_num: int):
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

    def creator(self) -> str:
        math_op = '{}{}{}{}{}'.format(
            self.__creat_math_op(self.first_level),  # 'xx +|-|*|/ xx'
            ' ',
            self.operator[random.randint(1, 4)],  # 随机选取运算符
            ' ',
            self.__creat_math_op(self.second_level),  # 'xx +|-|*|/ xx'
        )
        return math_op

    def __creat_math_op(self, level_choice: int) -> str:
        random_num = random.randint(0, 1)
        self.start_level += 1
        if self.start_level == level_choice:
            self.start_level = 0
            return random.randint(0, self.max_num)
        math_op = '{}{}{}{}{}{}{}'.format(
            self.__brackets(random_num, 0),  # '('
            NumCreat(self.max_num).choices_num(),  # 随机数
            ' ',
            self.operator[random.randint(1, 4)],  # 随机选取运算符
            ' ',
            self.__creat_math_op(level_choice),  # 'xx +|-|*|/ xx'
            self.__brackets(random_num, 1),  # ')'
        )
        self.start_level = 0
        return math_op

    def __brackets(self, random_num: int, choice: int) -> str:  # 决定括号是否填入
        if random_num:
            if choice:
                return ')'
            else:
                return '('
        return ''

    @property
    def math_op(self) -> str:  # 属性
        return self.creator()

    def creat_more(self, data_save):  # 迭代器
        op_num = 0
        while op_num < self.formula_num:
            math_op = self.creator()
            try:
                postfix, answer = AnalyOp.check_math_op(math_op)
                math_op = deal_math_op(math_op, list(postfix), answer, data_save)
                if math_op:
                    yield (math_op, answer)
                    op_num += 1
            except (ExceptError, ReduceError, ZeroDivisionError):
                pass
            self.__init_variable()

    def __init_variable(self):  # 初始化以下值
        self.start_level = 0
        self.level = random.randint(2, 4)
        self.first_level = random.randint(1, self.level - 1)
        self.second_level = self.level - self.first_level

    def __repr__(self):
        return f'Creat(max_num={self.max_num}, formula_num={self.formula_num})'


if __name__ == '__main__':
    t = Creat(1, 10000)
    data_save = DataSave().mathop_dict
    with TimeSum():
        for num, (math_op, answer) in enumerate(t.creat_more(data_save)):
            write_in_file(math_op, answer, num + 1)
