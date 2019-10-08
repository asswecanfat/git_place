import random


class Creat(object):
    def __init__(self, max_num, formula_num):
        self.max_num = max_num
        self.fromula_num = formula_num

    def creator(self):
        pass

    def __repr__(self):
        return f'Creat(max_num={self.max_num}, formula_num={self.fromula_num})'