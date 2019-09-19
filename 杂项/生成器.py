def myRev(x):
    ass = len(list(x))
    while 1:
        ass -= 1
        if ass < 0:
            raise StopIteration
        yield x[ass]
    
