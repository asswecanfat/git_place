import copy  # 该模块可进行深浅复制


a = [[1, 2, 3], [4, 5, 6]]
b = list(a)  # 与copy.copy()一样，但copy()可以复制任意对象
"""浅复制"""
print(f'a == b:{a == b}')
print(f'a is b:{a is b}')
a[0][0] = 5
print(f'a[0][0] = "x"   a :{a},b: {b}')

b = copy.deepcopy(a)
"""深复制"""
print(f'a == b:{a == b}')
print(f'a is b:{a is b}')
a[0][0] = 8
print(f'a[0][0] = "x"   a :{a},b: {b}')
