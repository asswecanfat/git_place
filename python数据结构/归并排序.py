from timeit import Timer
import random
def merge(a, b):#2路归并
    new_list = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] >= b[j]:
            new_list.append(b[j])
            j += 1
        else:
            new_list.append(a[i])
            i += 1
    new_list.extend(a[i:])
    new_list.extend(b[j:])
    return new_list

def merge_sort(a):
    m = int(len(a)/2)
    if len(a) <= 1:
        return a
    left = merge_sort(a[:m])
    right = merge_sort(a[m:])
    return merge(left,right)


a = [42,60,68,98,86,15,57]
print(merge_sort(a))
ms = Timer('merge_sort([random.randint(0,100) for i in range(0,20)])','from __main__ import merge_sort,random')
print(ms.timeit(1000))




