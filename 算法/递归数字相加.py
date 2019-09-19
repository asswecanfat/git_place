import random


def num_sum(list_):
    if len(list_) == 0:
        return 0
    else:
        return list_[0] + num_sum(list_[1:])


def num_count(list_):
    try:
        if list_[0]:
            pass
    except IndexError:
        return 0
    else:
        return 1 + num_count(list_[1:])


def find_list_max(list_):
    if len(list_) == 1:
        return list_[0]
    if find_list_max(list_[:len(list_)//2]) >= find_list_max(list_[len(list_)//2:]):
        return find_list_max(list_[:len(list_)//2])
    else:
        return find_list_max(list_[len(list_)//2:])


a = [random.randint(0, 10) for i in range(11)]
print(a)
print('{}{}'.format('列表总和：', num_sum(a)))
print('{}{}'.format('列表元素个数：', num_count(a)))
print('{}{}'.format('列表元素最大值：', find_list_max(a)))
