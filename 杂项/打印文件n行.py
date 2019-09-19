def sea(m = 1,n = -1):
    f.seek(0,0)
    b = 0
    for s in f:
        b += 1
        if b >= int(m):
            print(s)
        if b == int(n):
            break
f = open(str(input('请输入文件名：')))
a,c = input('请输入要打印的行数：').split(':')
if a == '':
    a = 1
if c =='':
    c = -1
sea(a,c)
