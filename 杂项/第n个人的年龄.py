def haha(n):
    if n == 1:
        return 10
    else:
        return haha(n-1)+2
ass = int(input('请输入：'))
print('第%d个人是%d岁' % (ass,haha(ass)))
    
    
