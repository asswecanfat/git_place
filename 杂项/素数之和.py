def shushu():
    ass = 0
    for i in range(10):
        for a in list(range(2, i-1)):
            if i % a != 0:
                ass = ass + i
    print(ass)
