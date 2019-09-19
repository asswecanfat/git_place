import random

def qsort(a):
    if len(a) > 1:
        b = a[0]
        less = [i for i in a[1:] if i <= b]
        gen = [i for i in a[1:] if i> b]
        return qsort(less) + [b] + qsort(gen)
    else:
        return a

a = [random.randint(0,100) for i in range(0,101)]
print(qsort(a))