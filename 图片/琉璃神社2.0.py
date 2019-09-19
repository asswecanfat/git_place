import re
import urllib.request
import time

def get_web(url):#获取页面信息
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0')
    reponse = urllib.request.urlopen(req)
    html = reponse.read().decode('utf-8')
    return html

def get_link(html):#从页面信息获取链接
    p = r'<a href="(.+)" rel="bookmark">(.+)</a></h1>'
    link = re.findall(p, html)
    ass = []#链接
    sea = []#标题
    for i in link:
        ass.append(i[0])
        sea.append(i[1])
    return (ass, sea)

def get_seed(url):#从ass中获取种子
    a = re.search(r'(?<=>).?(\d|[a-zA-z])+(?=(</.+>))',get_web(url))#(?<=>)(\d|[a-zA-z])+(?=(</.+>))
    seed = "magnet:?xt=urn:btih:" + a.group()
    return seed

def get_pit(html, ye):#从主页面中获取图片, ye为页数
    o = r'(?<!<img )src="(.+jpg)"'
    pit = re.findall(o, html)
    i = 1
    for u in pit:
        with open(str(ye) + '_' + str(i) + '.jpg', 'wb') as f:
            req = urllib.request.Request(u)
            req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0')
            reponse = urllib.request.urlopen(req)
            html = reponse.read()
            f.write(html)
        i += 1
        time.sleep(1)

def print_title(user, number):#输入想要抓取的窗口，number为想要爬取的第几页
    if user == '动画':
        return 'http://www.llss.tw/wp/category/all/anime/page/' + str(number) + '/'
    elif user == '漫画':
        return 'http://www.llss.tw/wp/category/all/comic/page/' + str(number) + '/'
    
#a, b = get_link(get_web('http://www.llss.tw/wp/'))

j = 1
shuru = input('请输入标签(可用标签:(动画，漫画))：')
num = int(input('输入页数：'))
if shuru == '':
    print('无该标签！！')
else:
    while j<=num:
        shur = print_title(shuru, j)
        get_pit(get_web(shur), j)
        a, b = get_link(get_web(shur))
        h = 0
        while h < len(a):
            sed = get_seed(a[h])
            if sed.find('熟') != -1:
                sed = sed.replace('熟', '')
                with open('合集' + '.txt', 'a', encoding='utf-8') as n:
                    n.write(str(j) + str(h+1)+ '.' + sed + '     ' + b[h] + '\n')
                h += 1
                time.sleep(1)
            elif sed.startswith('生') != -1:
                sed = sed.replace('生', '')
                with open('合集' + '.txt', 'a', encoding='utf-8') as n:
                    n.write(str(j) + str(h+1)+ '.' + sed + '     ' + b[h] + '\n')
                h += 1
                time.sleep(1)
            else:
                with open('合集' + '.txt', 'a', encoding='utf-8') as n:
                    n.write(str(j) + str(h+1)+ '.' + sed + '     ' + b[h] + '\n')
                h += 1
                time.sleep(1)
        j += 1
    print('获取完成！')
    
    

