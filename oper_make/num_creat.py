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
            return Fraction(self._interget)
        else:
            return Fraction(self.molecule, self.denominator)

    @staticmethod
    def fake2real_2_show(fake_num):
        molecule, denominator = list(map(int, re.findall(r'\d+', fake_num)))  # 分子，分母
        if denominator > molecule:
            return Fraction(molecule, denominator)
        return f"{molecule // denominator}'{Fraction(molecule % denominator, denominator)}"

    def __repr__(self):
        return f'NumCreat(max_num={self.max_num!r}'


if __name__ == '__main__':
    t = NumCreat(50)
    print(str(t.choices_num()))
