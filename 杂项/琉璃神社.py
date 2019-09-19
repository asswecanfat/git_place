import urllib.request
import re
import time

while True:
    ass = input('请输入一个琉璃网址(请输入ban终止程序！)：')
    if ass == 'ban':
        print("已终止！")
        break
    else:
        url = ass

        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0')
        reponse = urllib.request.urlopen(req)
        html = reponse.read().decode('utf-8')
        p = r'(?<=>).?([a-zA-Z]|\d)+(?=</.+>)'
        r = re.search(p, html)
        print(r.group())
        #with open('2.txt', 'w',encoding='utf-8') as f:
            #f.write(html)
