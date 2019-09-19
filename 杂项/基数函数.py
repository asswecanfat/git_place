def good(*ass):
    n = 0
    base = 3
    if ass[-1] == 5:
        base = 5
        can = sum(ass[:-1]) * 5
    else:
        can = sum(ass)* 3
    return can
d = []
while True:
    s = int(input('请输入参数：'))
    a = int(input('请输入1或0选择停止(1为继续，0为停止):'))
    d.append(s)
    if a == 0:
        break
print(good(*d))
