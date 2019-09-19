while True:
    see  = int(input('请输入十进制数：'))
    can = int(input('请输入你想转换成的进制：'))
    if can == 8:
        print('8进制数为：%o'%(see))
        continue
    if can == 16:
        print('16进制数为：%x'%(see))
        continue
    if can == 2:
        print('2进制数为：' ,bin(see))
        continue
    else:
        while True:
            can = int(input('错误！请重新输入进制：'))
            if can == 8:
                print('8进制数为：%o'%(see))
                break
            if can == 16:
                print('16进制数为：%x'%(see))
                break
            if can == 2:
                print('2进制数为：' ,bin(see))
                break

