def turn(n):
    a = '0'
    if n == 0:
        return a
    else:
        a = turn(n // 2)
        return a + str(n % 2)
n = int(input('请输入：'))
print(turn(n))

    
