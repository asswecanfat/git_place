import urllib.request

url = 'http://baidu.com'
heards = ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
          AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')
opener = urllib.request.build_opener()
opener.addheaders = [heards]
data = opener.open(url).read().decode('utf-8')
print(data)
