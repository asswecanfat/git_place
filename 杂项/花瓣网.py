import urllib.request
import urllib.parse
from http import cookiejar

loginurl = 'http://hm1.cnzz.com/heatmap.gif?id=1256903590&x=758&y=256&w=1519&s=1536x864&b=firefox&c=1&r=http://huaban.com/&a=0&p=http://huaban.com/&random=Sat Sep 22 2018 12:04:45 GMT+0800'

filename = 'cookie2.txt'
cookie = cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
pesponse = opener.open(loginurl)
cookie.save(ignore_discard = True, ignore_expires = True)

data = {}
data['email'] = '15521318232'
data['password'] = '99271727f'

req = urllib.request.Request(loginurl)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0')
rep = opener.open(req, urllib.parse.urlencode(data).encode('utf-8'))

if rep.geturl() == 'http://huaban.com/':
    print('登陆成功')
else:
    print('登陆失败')
