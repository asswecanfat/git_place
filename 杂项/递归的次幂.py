def power(x,y):
    if y == 0:
        return 1
    elif y == 1:
        return x
    else:
        return x * power(x,y-1)
x = int(input('请输入：'))
y = int(input('请输入次幂：'))
X = power(x,y)
print('%d的%d次方为：%d' % (x,y,X))
