def findstr(x,y):
    v = x.casefold()
    a = v.split(sep=' ')
    n = 0
    for b in a:
        if b == y:
            n+=1
        else:
            continue
    print('一共出现了%d次' % n)
x = str(input('请输入一段话：'))
y = str(input('请输入需要搜索的话：'))
findstr(x,y)
            
    
