import requests
from bs4 import BeautifulSoup
import json

def get_uel_data(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    reponse = requests.get(url,headers = headers)
    return reponse.content

def down_load_image(image_url, i):
    image_data = get_uel_data(image_url)
    with open("C:\\Users\\10248\\Desktop\\fgo\\" + str(i+1) + '.jpg', 'wb') as f:
        f.write(image_data)

def deal_data(txt):
    soup = BeautifulSoup(txt, 'lxml')
    image_url = soup.find_all('img', class_="yl-pic")
    servant_name = soup.find_all('a',target="_blank")
    for i in range(len(servant_name)):
        if servant_name[i].string == None:
            break
        else:
            new_i = servant_name[i].string.replace('\n','')
            down_load_image(image_url[i]['src'],i)
            print(new_i)
    return i

def deal_next_data(next_url, num):
    next_data = json.loads(get_uel_data(next_url).decode())['data']
    for i in range(len(next_data)):
        if (int(next_data[i].get('star')) >= 3) and (next_data[i].get('name') != '玛修·基列莱特' ):
            print(next_data[i].get('name'))
            down_load_image(next_data[i].get('icon'),num)
            num += 1
    return  num



def down_load_data(txt):
    '''print(json.loads(txt.decode())['data'])'''
    with open('C:\\Users\\10248\\Desktop\\2.txt','wb') as f:
        f.write(txt)

url = 'https://fgo.umowang.com/servant/list'
n_url = 'https://fgo.umowang.com/servant/ajax?card=&wd=&ids=&sort=12777&o=desc&pn='
num = deal_data(get_uel_data(url))
i = 2
while(i <=15):
    next_url = n_url + str(i)
    num = deal_next_data(next_url,num)
    i += 1


