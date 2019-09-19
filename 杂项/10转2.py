def tenexchange(x):
    a = x
    can = []
    m = '化为2进制为：'
    while True:
        ass = int(x % 2)
        x = (x - ass)/2
        can.append(ass)
        if x < 1:
            break
    can.reverse()
    for k in can:
        m = str(m)+str(k)
    print(str(m))
x = int(input('请输入：'))
tenexchange(x)  
