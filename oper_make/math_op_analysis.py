from collections import deque


class AnalyOp(object):  # 使用逆波兰表达式解析
    OPERATOR = ('+', '-', '*', '÷', '(', ')')  # 运算符常量

    def __init__(self, math_op):
        self.math_op = math_op.replace(' ', '')
        self.postfix_deque = deque()  # 后缀表达式栈
        self.operators_deque = deque()  # 运算符栈
        self.operators_priority = {  # 运算符优先级
            '+': 1,
            '-': 1,
            '*': 2,
            '÷': 2,
        }

    def mathop_to_postfix(self):
        """将中缀表达式转换为后缀表达式。"""
        for i in self.math_op:
            if self.__is_num(i):
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

    def __is_num(self, text):  # 判断是否为数字
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

    def __repr__(self):
        return f'AnalyOp(math_op={self.math_op})'


if __name__ == '__main__':
    a = AnalyOp('1 ÷ 2 - 3')
    print(a.mathop_to_postfix())
