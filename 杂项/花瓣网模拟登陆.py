import requests
from bs4 import BeautifulSoup
import re
import json

def get_user():#验证
    reponse = s.get(url, auth=('1024847824@qq.com', '99271727f'))
    soup = BeautifulSoup(reponse.text, 'html.parser')
    p = r'"username":"(.+)".+'
    p1 = r'(.+)", "urlname".+'
    get = re.findall(p, soup.text)
    get1 = re.findall(p1, get[0])
    return reponse.url

url = 'https://huaban.com/auth/'
data = {
    'email' : '1024847824@qq.com',
    'password' : '99271727f',
    '_ref' : 'frame'
    }
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Referer' : 'http://huaban.com'
           }
s = requests.Session()
reponse = s.post(url, data = data, headers = headers)
soup = BeautifulSoup(reponse.text, 'html.parser')
with open('C:\\Users\\10248\\Desktop\\Flower.txt', 'w' , encoding='utf-8') as f:
    f.write(soup.text)
try:
    p = r'"username":"(.+)".+'
    p1 = r'(.+)", "urlname".+'
    get = re.findall(p, soup.text)
    get1 = re.findall(p1, get[0])
except IndexError:
    print('需要验证！')
    get_user = get_user()
    if get_user == 'http://huaban.com/':
        print('登陆成功！可开始爬取！')
    else:
        print('登陆失败，请查找原因！')

    
