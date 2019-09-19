import easygui as f
import random as g
import sys
while 1:
    f.msgbox('欢迎进入猜数字游戏~',title='猜数字游戏',ok_button='没问题！')
    msg = '猜猜是哪个数字？'
    title = '答题环节'
    shu = g.randint(1,10)
    choices = [1,2,3,4,5,6,7,8,9,10]
    choice = f.choicebox(msg,title,choices)
    while int(choice) > int(shu):
        f.msgbox('大了大了~')
        choice = f.choicebox(msg,title,choices)
    else:
        f.msgbox('小了小了~')
        choice = f.choicebox(msg,title,choices)
    msg = '重新开始？'
    title = '选择'
    if f.ccbox(msg,title):
        pass
    else:
        sys.exit(0)
