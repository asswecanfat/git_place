from collections import namedtuple
from typing import NamedTuple


Test_car1 = namedtuple('Test_car1', ('color', 'price', 'name'))


class Test_car2(NamedTuple):
    color: str
    price: int
    name: str


test1 = Test_car1('red', 500000, 'Auto')
test2 = Test_car2('black', 600000, 'BWM')
print(test1, test2)
