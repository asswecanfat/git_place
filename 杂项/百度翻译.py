import urllib.parse
import urllib.request
import json


url = 'http://fanyi.baidu.com/extendtrans'

data = {}
data['from'] = 'zh'
data['query'] = '你好'
data['to'] = 'en'



data = urllib.parse.urlencode(data).encode('utf-8')


req = urllib.request.Request(url, data)
req.add_header('User-Agent', 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36')
reponse = urllib.request.urlopen(req)
reponse = reponse.read().decode('utf-8')
html = json.loads(reponse)


print(html)


