import random
#有序表
def binsearch(a, low, hight, keyword):
    mid = int((low + hight)/ 2)
    if low > hight:
        print('无法找到该关键字··')
        return -1
    if a[mid] == keyword:
        print('该关键字在 ' + str(mid+1) + ' 位置')
        return mid
    elif a[mid] > keyword:
        return binsearch(a, low, mid - 1, keyword)
    else:
        return binsearch(a, mid + 1, hight, keyword)

a = [random.randint(0, 1000) for i in range(100)]
a.sort()
print(a)
keyword = int(input('请输入要查找的数字：'))
binsearch(a,0,len(a),keyword)