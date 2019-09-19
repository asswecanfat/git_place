ass = input('请输入密码：')
i = 0
while True:
    if ass == '123456':
        print('成功登陆！')
        break
    else:
        see = input('密码错误，请重新输入密码：')
        string = list(see,)
        i+=1
        for x in string:
            if x == '*':
                i-=1
        if see == '123456':
            print('成功登陆！')
            break
        if i == 2:
            print('卡已冻结！')
            break
        

      
