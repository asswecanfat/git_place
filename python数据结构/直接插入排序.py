
def insertsort(a):
    for i in range(1,len(a)-1):
        if a[i+1] < a[i]:
            a[0] = a[i+1]
            j = i + 1
            while a[0] < a[j-1]:
                j -= 1
                a[j+1] = a[j]
            a[j] = a[0]
    print(a[1:])

a = [45,86,92,45,56,88,936,452,745,366,999]
insertsort(a)




