import urllib.request as urr
import chardet as c

respone = input('请输入URL：')
ass = urr.urlopen(respone).read()
v = c.detect(ass)

if v['encoding'] == 'utf-8':
    print('该网站编码方式是：' + v['encoding'])

elif v['encoding'] == 'GB2312':
    print('该网站使用的编码是：' + v['encoding'])
