def huiwen(n,m):   
    b = list(n)
    if len(n) == 1:
      return false 
    elif m==len(n)/2:
        return b[m] == b[int(len(n)-1-m)]
    else :
        return huiwen(n,m+1) and b[m] == b[int(len(n)-1-m)]
n = str(input('请输入：'))
a = 0
print(huiwen(n，a))
    
    
