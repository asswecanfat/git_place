string = list(range(100,1000))
for x in string:
    a = x % 10
    b = ((x % 100) - (x % 10 ))/10
    c = (x - (x%100))/100
    if x == a**3 + b**3 + c**3:
        print(x)
