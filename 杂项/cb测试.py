
def deal1(glist):
    i = 1
    if len(glist) > 2:
        b = i
        count = 0
        if glist[i] == '(':
            while 1:
                if glist[b] == '(':
                    count += 1
                if glist[b] == ')':
                    count -= 1
                    if count == 0:
                        break
                b += 1
        tou = glist[i:b+1]
        wei = '(' + glist[b+2:-1] + ')'
        print(tou)
        print(wei)
        deal1(tou)
        deal1(wei)
    else:
        return glist

glist = '((),((1,2,3,4),(2,3)))'
deal1(glist)
