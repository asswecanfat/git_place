def sure(x,y):
    b = []
    while True:
        if y > 1000 and x >=100:
            y = int(input('请重新输入上限：'))
        elif x < 100 and y < 1000:
            x = int(input('请重新输入下限：'))
        elif y > 1000 and x < 100:
            x = int(input('请重新输入下限：'))
            y = int(input('请重新输入上限：'))
        elif y <= 1000 and x >= 100:
            break
    for a in range(x,y):
        ass = (a%100-a%10)/10
        can = a % 10
        see = (a-a%100)/100
        if a == ass**3+can**3+see**3:
            b.append(a)
            print(a)
    if len(b) == 0:
        print('在这个范围内没有水仙花数')
print('x,y两个数均在100到1000以内')
x = int(input('请输入下限：'))
y = int(input('请输入上限：'))
sure(x,y)
        
    
