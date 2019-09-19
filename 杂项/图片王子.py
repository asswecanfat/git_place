import urllib.request
import re

url = 'https://image.baidu.com/'

req = urllib.request.Request(url)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0')
reponse = urllib.request.urlopen(req)
html = reponse.read().decode('utf-8')

ass = re.search(r'var Ihttps_agent_config', html)
print(ass)


