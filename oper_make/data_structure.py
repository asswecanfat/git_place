from typing import NamedTuple


class DataS(NamedTuple):  # 不可变元组
    math_op: str  # 子式
    op_list_index: int  # 索引
    answer: str  # 该整式的答案


if __name__ == '__main__':
    d = DataS('asd', 2, 'asd')
    print(d)
