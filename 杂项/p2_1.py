#p2_1.py
import random
ass = random.randint(1,10)
"""--- 第一个小游戏 ---"""
temp=input("不妨猜一下木吉现在心里想的是哪个数字:")
guess=int(temp)
n=1
while True :
    if guess ==ass:
        print("啊！That's good!")
        print("Ass we can!!")
    else:
        if guess>ass:
            print("哥，大了大了~~")
        else:
            print("嘿，小了小了~~")
    temp=input("啊！猜错了，请重新输入:")
    guess=int(temp)
    if guess ==ass:
        print("啊！That's good!")
        print("Ass we can!!")
    if n==4 or guess==ass:
        break
    n=n+1

print("不管怎样，木吉心里只有香蕉君，才没数字！！")
