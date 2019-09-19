def resis():
    ass = {}
    n = 0
    while True:
        if n == 0:
            print('欢迎来到XXX网站！')
            print('1.登陆')
            print('2.注册')
            a = int(input('请输入序号以选取功能：'))
            if a == 1:
                while n == 0:
                    b = str(input('请输入用户名：'))
                    if b not in ass:
                        print('无该用户名，请注册！')
                        break
                    else:
                        while n == 0:
                            c = str(input('请输入密码：'))
                            if c != ass[b]:
                                print('密码错误，请重新输入！')
                            else:
                                print('登陆成功！')
                                n = 1
            if a == 2:
                while True:
                    b = str(input('请输入用户名：'))
                    if b in ass:
                        print('该用户名已注册，请重新输入！')
                    else:
                        c = str(input('请输入密码：'))
                        ass[b] = c
                        print('注册成功！')
                        break
        else:
            break
resis()
            
                
            
