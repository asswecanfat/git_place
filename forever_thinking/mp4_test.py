import json
import random
import time

import requests
from bs4 import BeautifulSoup

s = requests.Session()
IP_list = []
with open(r'C:\Users\10248\Desktop\test\ip_can_use.txt', 'r', encoding='utf-8') as g:
        while 1:
            data = str(g.readline())
            if data != '':
                IP = data.split()[0] + ':' + data.split()[1]
                IP_list.append(IP)
            else:
                break
proxy = random.choice(IP_list)
proxies = {'http': 'http://'+proxy, 'https': 'https://'+proxy}
url_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
requests_url = 'http://ddrk.me/'


def download_mp4(new_headers, request_url, num, need_mp4):
    reponse = s.get(request_url, headers=new_headers, proxies=proxies)
    with open('C:\\Users\\10248\\Desktop\\test\\' + need_mp4 + str(num) + '.mp4', 'wb') as f:
        f.write(reponse.content)


def get_url_soul(new_headers, request_url):
    reponse = s.get(request_url, headers=new_headers, allow_redirects=False, proxies=proxies)
    with open(r'C:\Users\10248\Desktop\test\new_url_message.txt', 'wb') as f:
        f.write(reponse.content)
    return reponse.text


def get_url_new_soul(new_headers, request_url):
    reponse = s.get(request_url, headers=new_headers, allow_redirects=False, proxies=proxies)
    return reponse.headers


def get_mp4_url_from_text(text):
    mp4_url = {}
    soup = BeautifulSoup(text, 'lxml')
    try:
        hot_list = soup.find_all(class_="post-box-list")
        mp4_url_list = hot_list[0].find_all(class_="post-box-title")
        print('热映中：')
        for i in range(len(mp4_url_list)):
            key = str(i+1) + '.' + mp4_url_list[i].a.string
            value = mp4_url_list[i].a['href']
            mp4_url[key] = value
            print(key)
    except AttributeError:
        print('网页某些属性已更改，请重新定位！！')
    return mp4_url


def get_mp4_address(mp4_text, value):  # 获得.mp4的网址
    mp4_re_url = []
    new_url = []
    soup = BeautifulSoup(mp4_text, 'lxml')
    get_mp4_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                       'Connection': 'keep - alive',
                       'Accept': '* / *',
                       'Origin': 'http://ddrk.me',
                       'Referer': value,
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-CN,zh;q=0.9'
                       }
    try:
        mp4_co = soup.find_all(class_='wp-playlist-script')
        data = json.loads(mp4_co[0].text)
        _id = data['tracks']
        for i in _id:
            re_url = 'http://v3.ddrk.me:9543/video?id=' + i['src'] + '&type=json'
            mp4_re_url.append(re_url)
        for _i in mp4_re_url:
            data_url = json.loads(get_url_soul(get_mp4_headers, _i))
            new_url.append(data_url['url'])
            time.sleep(random.randint(0, 5))
    except (AttributeError, KeyError):
        print('IP被封，请重新换IP！！')
    return new_url


def main():
    mp4_url = get_mp4_url_from_text(get_url_soul(url_headers, requests_url))
    need_value = None
    need_mp4 = input('请输入想要的片：')
    for key, value in mp4_url.items():
        if need_mp4 in key:
            need_value = value
            print(value)
            break
    mp4_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
                   'Accept': '*/*', 'Accept-Encoding': 'identity;q=1, *;q=0',
                   'Accept-Language': 'zh-CN,zh;q=0.9',
                   'chrome-proxy': 'frfr',
                   'Range': 'bytes=0-',
                   'Referer': need_value,
                   'Connection': 'keep-alive',
                   'Host': 'g.shumafen.cn'
                   }
    mp4_text = get_url_soul(url_headers, need_value)
    new_url = get_mp4_address(mp4_text, need_value)
    for num in range(len(new_url)):
        new_a = get_url_new_soul(mp4_headers, new_url[num])
        final_mp4_url = get_url_new_soul(mp4_headers, 'http://g.shumafen.cn/api/' + new_a['location'][6:])['location']
        download_mp4(mp4_headers, final_mp4_url, num + 1, need_mp4)
        print('下载成功')


main()
