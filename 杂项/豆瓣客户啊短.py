import urllib.request
import urllib.parse
from http import cookiejar
import re

loginurl = 'https://www.douban.com/accounts/login'

cookie = cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
pon = opener.open('https://accounts.douban.com/login')
print(pon.geturl())



def get_html(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0')
    rep = opener.open(req).read().decode('utf-8')
    return rep

def get_pit(url):
    d = get_html(url)
    a = r'<img id="captcha_image" src="(.+)" alt="captcha" class="captcha_image"/>'
    b = re.findall(a, d)
    c = b[0]
    asx = urllib.request.Request(c)
    asx.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0')
    ass = opener.open(asx)
    sea = ass.read()
    with open('1.jpg', 'wb') as f:
        f.write(sea)

def get_value(url):
    d = get_html(url)
    a = r'<input type="hidden" name="captcha-id" value="(.+)"/>'
    b = re.findall(a, d)
    c = b[0]
    return c

'''with open('1.txt', 'w', encoding='utf-8') as f:
    f.write(get_html(loginurl))'''

c = get_value(loginurl)
get_pit(loginurl)
we = input('请输入验证码：')

data = {}
data["captcha-id"] = c
data["captcha-solution"] = we
data['form_email'] = '1024847824@qq.com'
data['form_password'] = '99271727f'
data["login"] = "登录"
data['redir'] = 'https://www.douban.com/'
data['source'] = 'index_nav'

req = urllib.request.Request(loginurl)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0')
rep = opener.open(req, urllib.parse.urlencode(data).encode('utf-8'))
html = rep.read().decode('utf-8')

print(rep.geturl())
    

'''if rep.geturl() == 'https://www.douban.com/':
    print('登陆成功')
    p = r'<span>(\w{2})\w+</span>'
    list1 = re.findall(p, html)
    print('登陆的账号为：' + list1[0])
else:
    print('登陆失败')'''


