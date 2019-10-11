from typing import NamedTuple


class DataS(NamedTuple):  # 不可变元组
    math_op: str  # 子式
    op_list_index: int  # 索引
    answer: str  # 该整式的答案
