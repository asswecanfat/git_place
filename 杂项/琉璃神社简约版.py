import requests as re_
from bs4 import BeautifulSoup

ass = re_.get('https://movie.douban.com/chart')
'''with open('moive.txt', 'w') as f:
    f.write(ass.text)'''
sea = BeautifulSoup(ass.text, 'html.parser')
for i in sea.find_all('a'):
    print(i.string)
