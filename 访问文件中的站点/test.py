import urllib.request as urr
import chardet as c

with open('urls.txt', 'r') as f:
    i = 1
    while i<6:
        a = f.readline()
        sea = a.replace('\n', '')
        can = 'url' + str(i) + '.txt'
        respone = urr.urlopen(a).read()
        v = c.detect(respone)
        if v['encoding'] == 'utf-8':
            html = respone.decode('utf-8')
        elif v['encoding'] == 'GB2312':
            html = respone.decode('GBK')
        with open(can, 'a',encoding='utf-8') as b:
            b.write(html)
        i += 1

        
print('已经完成')
