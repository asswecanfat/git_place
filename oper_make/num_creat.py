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
        s_molecule, s_denominator = NumCreat.gcd(molecule, denominator)
        if s_denominator > s_molecule:
            return f"{Fraction(s_molecule, s_denominator)}"
        else:
            if s_molecule % s_denominator == 0:
                return f'{s_molecule // s_denominator}'
            return f"{s_molecule // s_denominator}'{Fraction(s_molecule % s_denominator, s_denominator)}"

    @staticmethod
    def gcd(molecule, denominator):  # 最简化分数
        max_num, min_num = (molecule, denominator) if molecule > denominator else (denominator, molecule)
        while True:
            remainder = max_num % min_num
            if remainder == 0:
                return molecule // min_num, denominator // min_num
            max_num, min_num = min_num, remainder

    def __repr__(self):
        return f'NumCreat(max_num={self.max_num!r}'


if __name__ == '__main__':
    t = NumCreat(50)
    print(t.fake2real_2_show('2/2'))
