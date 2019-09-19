import urllib.request, urllib.parse
import json
import random
import time

def main():
    while True:
        
        cen = input('请输入需要翻译的内容("输入bang结束程序")：')
        if cen == 'bang':
            break
        
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        data = {}
        data['i'] = cen
        data['from'] = 'AUTO'
        data['to'] = 'AUTO'
        data['smartresult'] = 'dict'
        data['client'] = 'fanyideskweb'
        data['doctype'] = 'json'
        data['version'] = '2.1'
        data['keyfrom'] = 'fanyi.web'
        data['action'] = 'FY_BY_REALTIME'
        data['typoResult'] = 'true'

        head = {}
        head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'

        '''list1 = ['222.76.204.110:808', '103.38.197.42:53281', '183.129.207.78:18118', '120.237.14.198:53281']
        req = random.choice(list1)
        proxy_support = urllib.request.ProxyHandler({'http':req})
        opener = urllib.request.build_opener(proxy_support)
        opener.addheaders = [('User-Agent', head)]
        urllib.request.install_opener(opener)'''#代理有问题


        data = urllib.parse.urlencode(data).encode('utf-8')
        ass = urllib.request.Request(url, data, head)
        respone = urllib.request.urlopen(ass)
        html = respone.read().decode('utf-8')
        tar = json.loads(html)
        print('翻译结果为：%s' % tar['translateResult'][0][0]['tgt'])

        time.sleep(2)
    print('退出成功！')




if __name__ == '__main__':
    main()
    

    
