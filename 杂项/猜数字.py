import easygui as g
import sys
import random as a
g.msgbox('来玩个猜数字游戏吧~')
ass = g.integerbox(msg = '请输入1~10任一个数字',lowerbound = 1,upperbound = 10)
shu = a.randint(1,10)
while 1:
    if shu > ass:
        g.msgbox('小了小了~')
        ass = g.integerbox(msg = '请输入1~10任一个数字',lowerbound = 1,upperbound = 10)
    elif shu == ass:
        g.msgbox('猜对咯！')
        break
    else:
        g.msgbox('大了大了！')
        ass = g.integerbox(msg = '请输入1~10任一个数字',lowerbound = 1,upperbound = 10)       
if g.ccbox(msg = '你希望重新开始吗？'):
    pass
else:
    sys.exit(0)


    
