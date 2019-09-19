import urllib.request
import re
import time


url = str(input("请输入花瓣网的一个版面："))

def get_web(url):#获取页面信息
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36')
    reponse = urllib.request.urlopen(req)
    html = reponse.read().decode('utf-8')
    return html
    
def getin_list(html):#获取图片页面，所有图片的地址挖掘完成
    ass = []
    p = re.compile(r'"pin_id":(\d+)')
    a = re.findall(p, html)
    for i in a:
        k = 'http://huaban.com/pins/' + i +'/'
        ass.append(k)
    return ass

def get_pit(html):#获得图片地址
    sea = re.compile(r'"key":"([\d|\w]+-[\d\w]+)"')
    can = re.findall(sea, html)
    r = 'http://img.hb.aicdn.com/' + can[1] + '_fw658'
    return r

def download_pit(url):#下载图片
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36')
    reponse = urllib.request.urlopen(req)
    html = reponse.read()
    return html

key = getin_list(get_web(url))

baby = []
for we in key:
    baby.append(get_pit(get_web(we)))
    time.sleep(1)

i = 1
for f in baby:
    with open(str(i)+'.jpg', 'wb') as o:
        o.write(download_pit(f))
    print('下载成功！')
    i += 1
    time.sleep(1)


