__all__ = ['youxi']
import easygui as g
import random as a
import sys

#弹出用户登陆窗口
def youxi():
    while 1:
        ass = '用户'
        can = '密码'
        s = g.multpasswordbox('请输入你的账号和密码', '账号输入', [ass,can])
        if s[0] == '3117004628' and s[1] == '123':
            g.msgbox('欢迎来到你的专属sex空间~~~', ok_button='oh~yeah~')
            break
        else:
            g.msgbox('输入错误，无法享受sex空间！')
    #猜数字
    g.msgbox('来玩个猜数字游戏吧~,猜对了才有福利哦', '猜数字', '嗯？！')
    g.msgbox('警告：该游戏只能玩三次，三次不过的话就没福利了！！！', '猜数字', ok_button='好的，我知道了！')
    ass = g.integerbox(msg = '请输入1~10任一个数字',lowerbound = 1,upperbound = 10)
    shu = a.randint(1,10)
    i = 0
    while 1:
        if shu > ass:
            g.msgbox('小了小了~', ok_button='知道了')
            i += 1
            ass = g.integerbox(msg = '请输入1~10任一个数字',lowerbound = 1,upperbound = 10)
        elif shu == ass:
            g.msgbox('猜对咯！')
            break
        elif shu < ass:
            g.msgbox('大了大了！', ok_button='知道了')
            i += 1
            ass = g.integerbox(msg = '请输入1~10任一个数字',lowerbound = 1,upperbound = 10)
        else:
            if i == 2:
                g.msgbox('与福利擦身而过了，下次加油吧', ok_button='知道了')
                sys.exit(0)    
    #通过游戏，提问考验
    sea = g.buttonbox('你渴望奈子么？？', '选择吧，让我听到你的心声！', image='gg.gif', choices=('是的！', '额..(⊙o⊙）其实我更喜欢屁股~'))
    if sea == '是的！':
        g.msgbox('恭喜你！获得奈子！')
        we = g.buttonbox('怎么样？', image='sex1.gif', choices=('还可以', '我觉得不行！'))
        if we == '我觉得不行！':
            g.msgbox('滚犊子！再见！', '恩~，不要嘛~')
            sys.exit(0)
        else:
            g.msgbox('祝你身体愉快，生活健康，再见~', '我还想要怎么办？？？')
            sys.exit(0)
    else:
        g.msgbox('再见，没有福利了！', '...其实奈子是不错的！！')
        sys.exit(0)

if __name__ == '__main__':
    youxi()

    


