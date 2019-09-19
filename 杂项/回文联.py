def huiwen():
    b = []
    n = -1
    s = list(a)
    for x in s:
        b.append(s[n])
        n-=1
        if n == -len(s)-1:
            break
    if s == b:
        print('这是回文联！')
    else:
        print('这不是回文联！')
a = str(input('请输入一行字，判断是否为回文联：'))
huiwen()
