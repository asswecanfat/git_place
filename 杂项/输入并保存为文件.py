a = []
d = 1
while True:
    b = str(input('请输入：'))
    a.append(b)
    file_c = 'text_'+str(d)+'.txt'
    f = open(file_c,'w')
    f.writelines(a)
    f.close()
    d += 1
    print('输入成功！')
    k = int(input('请输入1或0来决定停止（1：继续，0：停止）：'))
    if k == 0:
        break
        
    
