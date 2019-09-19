import time

first_time = time.time()
a = 0
while a <= 1000:
    b = 1000 - a
    while b>= 0:
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print("a,b,c:%d %d %d" % (a,b,c))
        b -= 1
    a += 1
end_time = time.time()
print('use time:%d' % (end_time - first_time))