import urllib.request
import urllib.parse
from http import cookiejar
import re

loginurl = 'http://jxfw.gdut.edu.cn/'

cookie = cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
pon = opener.open(loginurl)

def get_html(url):#获取页面信息
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0')
    rep = opener.open(req).read().decode('utf-8')
    return rep

def get_pit(url):#获取验证码图片
    d = get_html(url)
    a = r'src="(.+)"'
    b = re.findall(a, d)
    print(b[1])
    '''asx = urllib.request.Request(c)
    asx.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0')
    ass = opener.open(asx)
    sea = ass.read()
    with open('2.jpg', 'wb') as f:
        f.write(sea)'''


get_pit(loginurl)
'''rep = get_html(loginurl)
with open('1.txt', 'w', encoding='utf-8') as f:
    f.write(rep)'''

#checkma = input('请输入验证码：')


'''if html == 'http://jxfw.gdut.edu.cn/login!welcome.action':
    print('登陆成功')
else:
    print('登陆失败')'''
