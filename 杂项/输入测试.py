def int_input(prompt=''):
    while True:
        try:
            int(input(prompt))
            break
            print(int(input(prompt)))
        except ValueError:
            print('出错，您输入的不是整数！')
 
int_input('请输入一个整数：')
