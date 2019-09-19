import requests
from bs4 import BeautifulSoup
import  re

def get_data(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    reponse = requests.get(url,headers = headers)
    return reponse.content

def deal_image(data):
    with open('C:\\Users\\10248\\Desktop\\1.txt','wb') as f:
        f.write(data)
def deal_data(data):
    soup = BeautifulSoup(data,'lxml')
    soup1 = soup.find_all(class_="anchor-name")
    soup2 = soup.find_all(class_="v-middle dp-i-block")
    soup3  =soup.find_all(class_="room-title ts-dot-4")
    for i in range(len(soup1)):
        print(str(i+1) + '.' + soup3[i].string + '   ' + soup1[i].string + '  人数：' + soup2[i].string)


try:
    data = get_data('https://live.bilibili.com/')
except BaseException as e:
    print('error')
else:
    deal_data(data)