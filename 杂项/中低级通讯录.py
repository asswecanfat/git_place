def fain():
    while True:
        s = str(input('请输入人名搜索手机号：'))
        if s in ass:
            print(ass[s])
        else:
            print('查无此人！')
        print('1:继续','0;终止')
        k = int(input('请选择：'))
        if k == 0:
            break
def up():
    while True:
        m = str(input('请输入联系人姓名：'))
        v = str(input('请更改联系电话：'))
        if m in sad:
            ass[m] = v
            print('更改成功！')
        else:
            print('查无此人！')
        n = int(input('请输入：1.继续 2.终止  ：'))
        if n == 2:
            break
        
ass = {}
while True:
    print('请选择功能：')
    print('1.新增联系人。')
    print('2.查看已有联系人。')
    print('3.查找联系人手机号。')
    print('4.更新联系人信息')
    print('5.退出系统。')
    b = int(input('请输入数字选取功能：'))
    if b == 1:
        sad = []
        n = str(input('请输入姓名：'))
        a = str(input('请输入手机号：'))
        ass[n] = a
        can = sad.append(n)
        print('存储成功！')
    if b == 2:
        print(ass)
    if b == 3:
        fain()
    if b == 4:
        up()
    if b == 5:
        print('感谢您的使用！')
        break
    

