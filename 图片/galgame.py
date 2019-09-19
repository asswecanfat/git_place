import urllib.request

url = 'https://www.mygalgame.com/yufaqinggaolengmhuichangdeguojitianmixueyuanshenghuo.html'

data = {'e_secret_key' : 'A665'}
req = urllib.request.Request(url, data)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0')
reponse = urllib.request.urlopen(req)
html = reponse.read().decode('utf-8')

with open('3.txt', 'w', encoding='utf-8') as f:
    f.write(html)
