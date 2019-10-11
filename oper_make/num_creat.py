from fractions import Fraction
import random
import re


class NumCreat(object):
    def __init__(self, max_num):
        self.max_num = max_num
        self._interget = random.randint(0, self.max_num)
        self.denominator = random.randint(1, self.max_num)  # 分母
        self.molecule = random.randint(1, self.max_num)  # 分子

    def choices_num(self, random_choices=random.randint(1, 10)):
        if random_choices > 3:
            return self._interget
        else:
            return Fraction(self.molecule, self.denominator)

    @staticmethod
    def fake2real_2_show(fake_num):
        molecule, denominator = list(map(int, re.findall(r'\d+', fake_num)))  # 分子，分母
        s_molecule, s_denominator = NumCreat.is_simplest_fraction(molecule, denominator)
        if s_denominator > s_molecule:
            return f"{Fraction(s_molecule, s_denominator)}"
        else:
            if s_molecule % s_denominator == 0:
                return f'{s_molecule // s_denominator}'
            return f"{s_molecule // s_denominator}'{Fraction(s_molecule % s_denominator, s_denominator)}"

    @staticmethod
    def is_simplest_fraction(molecule, denominator):  # 最简化分数
        min = (lambda x, y: x if x < y else y)(molecule, denominator)
        hcf = 1  # 最大公约数，默认为1
        for i in range(1, min + 1):
            if not (molecule % i or denominator % i):
                hcf = i
        return molecule // hcf, denominator // hcf

    def __repr__(self):
        return f'NumCreat(max_num={self.max_num!r}'


if __name__ == '__main__':
    t = NumCreat(50)
    print(t.fake2real_2_show('1/5'))
