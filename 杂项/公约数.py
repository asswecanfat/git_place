def gcd(x,y):
    if x == y:
        return x
    else:
        a = max(x,y)
        b = min(x,y)
        while True:
            ass = a % b
            a = b
            b = ass
            if ass == 0:
                break
        return a
x = int(input('请输入：'))
y = int(input('请输入：'))
print(gcd(x,y))
        
    
    
