f1 = open('text_1.txt')
f2 = open('text_2.txt')
n = 1
m = 1
lines1 = list(f1)
lines2 = list(f2)
print(lines1)
print(lines2)
for each_line1 in lines1:
    m = 1
    for each_line2 in lines2:
        if each_line1 != each_line2:
            print('text_1的第%d行与text_2的第%d行不同' % (n,m))
            m += 1
        else:
            m += 1
            continue
    n += 1
f1.close()
f2.close()
