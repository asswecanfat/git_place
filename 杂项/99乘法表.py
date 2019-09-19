num = 9
nUm = 10
while num:
    a = nUm - (nUm - num)
    while a > 0:
        print('%d*%d=%d' % (num,a,num*a),end='  ')
        a -= 1
    num -= 1
    print()
