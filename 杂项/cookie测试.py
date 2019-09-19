import urllib.parse
import urllib.request
from http import cookiejar

#声明一个CookieJar对象实例来保存cookie
cookie = cookiejar.CookieJar()

#利用urllib库中的request的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib.request.HTTPCookieProcessor(cookie)

#通过handler来构建opener
opener = urllib.request.build_opener(handler)

#此处的open方法同urllib的urlopen方法，也可以传入request
response = opener.open('https://www.douban.com/')

for item in cookie:
    print('name= ' + item.name)
    print('value= ' + item.value)
