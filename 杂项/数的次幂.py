def power(x,y):
    ass = 1
    if y == 0:
        ass = 1
    else:
        for i in range(y):
            ass = ass * x
    return ass
x = int(input('请输入数字：'))
y = int (input('请输入次幂：'))
print(power(x,y))
    
