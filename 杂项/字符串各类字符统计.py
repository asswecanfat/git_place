def tongji():
    n = 0
    m = 0
    r = 0
    i = 0
    b = a.casefold()
    s = list(b)
    for x in s:
        if x == ' ':
            n+=1
        elif 122 >= int(ord(x)) and int(ord(x)) >= 97:
            m+=1
        elif x.isdigit() == True:
            r+=1
        else:
            i+=1
    print('空格有%d个'%n)
    print('字母有%d个'%m)
    print('数字有%d个'%r)
    print('其他字符有%d个'%i)
a = str(input('请输入一段字符串：'))
tongji()
