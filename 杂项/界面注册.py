import easygui as g
import sys
can = {'123456':'123456'}
sea = []
ha = ['123456']
g.msgbox('欢迎来到账号注册~')
chioses = ['1.注册','2.登陆']
ass = g.choicebox('请选择功能：',choices=chioses)
if ass == '1.注册':
    c = str(g.enterbox('请输入账号：'))
    d = str(g.enterbox('请输入密码：'))
    sea = sea.append(c)
    ha = ha.append(d)
    can[c] = d
    g.msgbox('注册成功！')
else:
    e = str(g.enterbox('请输入账号：'))
    f = str(g.passwordbox('请输入密码：'))
    while e not in can:
        g.msgbox('没有该账号，请注册！')
        c = str(g.enterbox('请输入账号：'))
        d = str(g.enterbox('请输入密码：'))
        sea = sea.append(c)
        ha = ha.append(d)
        can[c] = d
    while f not in ha:
        g.msgbox('密码错误，请重新输入！')
        f = str(g.passwordbox('请输入密码：'))
    g.msgbox('登陆成功！')
if g.ccbox('重新登陆？'):
    pass
else:
    sys.exit(0)
    
