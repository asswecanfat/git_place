#coding:gb2312
import requests
from bs4 import BeautifulSoup
import json
import re

url = 'https://www.gracg.com/login/index_do'
url1 = 'https://www.gracg.com/'
headers = {'user-agent':'ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',\
'referer':'https://www.gracg.com/login'}
s = requests.Session()
data = {'username':'15521318232', 'pwd':'99271727f', 'type':'login'}
reponse = s.post(url, headers = headers, data = data)
reponse1 = s.get(url1)
with open('C:\\Users\\10248\\Desktop\\1.txt', 'w', encoding='utf-8') as d:
	d.write(reponse.text)
with open('C:\\Users\\10248\\Desktop\\1.txt', 'r') as f:
	message = json.load(f)
with open('C:\\Users\\10248\\Desktop\\userdata.txt', 'w', encoding='utf-8') as g:
	g.write(reponse1.text)
print(message['message'])
soup = BeautifulSoup(reponse1.text, 'html.parser')
soup1 = soup.find_all('div', style='text-align: center;background: #ddd;padding: 3px;width: 118px;overflow: hidden;font-size: 12px')
print('登陆的账号为：'+soup1[0].get_text())





