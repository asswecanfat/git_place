import random

def ki_sort(a,n):
    pos, count = [0 for i in range(10)], [0 for i in range(10)]
    pos[0] = 0
    for c in range(len(a)):
        count[int(a[c][n-1])] += 1
    for b in range(1,10):
        pos[b] = count[b-1] + pos[b-1]
    new_a = [0 for i in range(len(a))]
    for d in range(len(a)):
        new_a[pos[int(a[d][n-1])]] = a[d]
        pos[int(a[d][n-1])] += 1
    a = new_a
    if n > 1:
        return ki_sort(a,n-1)
    else:
        return a


a = [str(random.randint(100000000,999999999)) for i in range(10000)]
a = ki_sort(a,4)
print(a)




