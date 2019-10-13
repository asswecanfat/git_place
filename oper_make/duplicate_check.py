from data_sturct import Node
from collections import deque
from math_op_analysis import AnalyOp
from fractions import Fraction


def creat_tree(postfix_deque):  # 创建统一的二叉树
    node = deque()
    for i in postfix_deque:
        if AnalyOp.is_num(i):
            node.append(Node(num=i, answer=i, min=i))
        else:
            max_num, min_num = node.pop(), node.pop()
            if i != '÷' and i != '-':
                if max_num.answer == min_num.answer:
                    max_num, min_num = (max_num, min_num) if Fraction(max_num.min) >= Fraction(min_num.min) \
                        else (min_num, max_num)
                else:
                    max_num, min_num = (max_num, min_num) if Fraction(max_num.answer) > Fraction(min_num.answer) \
                    else (min_num, max_num)
            op = Node(operator=i,
                      right_child=max_num,
                      left_child=min_num,
                      answer=AnalyOp.operation_func(i)(min_num.answer, max_num.answer),
                      min=min_num.min,)
            node.append(op)
    return node.pop()


def isEqual(t1,t2):  # 比较两棵树是否一样
    if not t1 and not t2:
        return True
    if not t1 and t2:
        return False
    if t1 and not t2:
        return False
    if t1.answer == t2.answer and t1.operator == t2.operator:
        return isEqual(t1.left_child,t2.left_child) and isEqual(t1.right_child,t2.right_child)
    else:
        return False


if __name__ == '__main__':
    t1 = creat_tree(['1','4','*'])
    t2 = creat_tree(['2','2','*'])
    print(isEqual(t1, t2))

