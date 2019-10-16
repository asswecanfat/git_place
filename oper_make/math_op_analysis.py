from collections import deque
from fractions import Fraction
from op_error import ExceptError, ReduceError
from copy import deepcopy
import re


class AnalyOp(object):  # 使用逆波兰表达式解析
    OPERATOR = ('+', '-', '*', '÷', '(', ')')  # 运算符常量

    def __init__(self, math_op):
        self.math_op = math_op.replace('(', '( ').replace(')', ' )')
        self.math_op = self.math_op.split()
        self.postfix_deque = deque()  # 后缀表达式栈
        self.operators_deque = deque()  # 运算符栈
        self.operators_priority = {  # 运算符优先级
            '+': 1,
            '-': 1,
            '*': 2,
            '÷': 2,
        }

    def __clear_deque(self):  # 用于清空栈
        self.postfix_deque.clear()
        self.operators_deque.clear()

    def mathop_to_postfix(self):
        """将中缀表达式转换为后缀表达式。"""
        for i in self.math_op:
            if self.is_num(i):
                self.postfix_deque.append(i)
            elif i in self.OPERATOR:
                if i == '(':
                    self.operators_deque.append(i)
                elif i == ')':
                    self.__pop_to_left_bracket()
                else:
                    self.__compare_and_pop(i)
        self.__pop_rest()
        return self.postfix_deque

    @staticmethod
    def is_num(text):  # 判断是否为数字
        if '/' in text:
            return True
        return text.isdigit()

    def __pop_to_left_bracket(self):
        """依次弹栈并追加到后缀表达式，直到遇到左括号为止。"""
        while self.operators_deque:
            operator = self.operators_deque.pop()
            if operator == '(':
                break
            self.postfix_deque.append(operator)

    def __compare_and_pop(self, text):
        """比较优先级并进行相应操作。"""
        if not self.operators_deque:
            self.operators_deque.append(text)
            return
        while self.operators_deque:
            operator = self.operators_deque.pop()
            if operator == '(':
                self.operators_deque.append('(')
                self.operators_deque.append(text)
                return
            elif self.operators_priority[text] > self.operators_priority[operator]:
                self.operators_deque.append(operator)
                self.operators_deque.append(text)
                return
            elif text == operator:
                self.postfix_deque.append(operator)
            else:
                self.postfix_deque.append(operator)
        self.operators_deque.append(text)

    def __pop_rest(self):
        """弹出所有剩余的运算符，追加到后缀表达式。"""
        while self.operators_deque:
            self.postfix_deque.append(self.operators_deque.pop())

    def parse_out_son(self):
        """只解析出有优先级的子式"""
        postfix = deepcopy(self.mathop_to_postfix())
        num_deque = deque()
        son_op_list = []
        answer = None
        for i in self.postfix_deque:
            if self.is_num(i):
                num_deque.append(i)
            else:
                right_num = num_deque.pop()
                left_num = num_deque.pop()
                son_op = f'{left_num}{i}{right_num}'
                son_op_list.append(son_op)
                answer = self.operation_func(i)(left_num, right_num)
                num_deque.append(answer)
        self.__clear_deque()
        return son_op_list, postfix, str(answer)

    @staticmethod
    def operation_func(operator):  # 选择运算方法
        operation_dict = {
            '+': lambda x, y: Fraction(x) + Fraction(y),
            '-': lambda x, y: Fraction(x) - Fraction(y),
            '*': lambda x, y: Fraction(x) * Fraction(y),
            '÷': lambda x, y: Fraction(x) / Fraction(y),
        }
        return operation_dict[operator]

    @staticmethod
    def check_math_op(math_op):  # 检查分解成的子式的合法性
        mop = AnalyOp(math_op)
        op_list, postfix, answer = mop.parse_out_son()
        for i in op_list:
            left_num, right_num = re.split(r'[+\-*÷]', i)
            if '÷' in i:
                if Fraction(left_num) > Fraction(right_num) or right_num == 0:
                    raise ExceptError
            if '-' in i:
                if Fraction(left_num) < Fraction(right_num):
                    raise ReduceError
        return postfix, answer

    def __repr__(self):  # 用于测试
        return f'AnalyOp(math_op={self.math_op!r})'


if __name__ == '__main__':
    a = AnalyOp('(1/2 ÷ 2) + (3 * 6)')
    print(a.mathop_to_postfix())
    print(a.parse_out_son())
