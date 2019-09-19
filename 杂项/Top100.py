import requests
from bs4 import BeautifulSoup
import re

def mao_yan_url():#第wen_num页
    maoyan_url = []
    for i in range(0,10):
        m_url = 'http://maoyan.com/board/4?offset=' + str(i) + '0'
        maoyan_url.append(m_url)
    return maoyan_url

def get_m_url_data(web_url):#获取maoyan_url中每个url的data
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    reponse = requests.get(web_url, headers = headers)
    return reponse.text

def file_data(txt):#保存文件测试
    with open('C:\\Users\\10248\\Desktop\\top100.txt', 'w', encoding='utf-8') as f:
        f.write(txt)

def re_mathod(txt, n):#使用正则,n为页数
    p = r'<p class="name"><a href=".+?" title=".+?" data-act="boarditem-click" data-val=".+?">(.+?)</a></p>.*?<p .+?>(.+?)</p>'
    pattern = re.compile(p, re.S)
    moives_people = re.findall(pattern, txt)
    people = []
    for i in range(len(moives_people)):
        people.append(moives_people[i][1].replace('\r','').replace('\n','').replace('\t',''))
    for a in range(len(moives_people)):
        print(str(a+1+n) + '.' +moives_people[a][0] + people[a])


maoyan_url = mao_yan_url()
print('猫眼中Top100的电影：\n')
for i in range(len(maoyan_url)):
    n = 10*i
    txt = get_m_url_data(maoyan_url[i])
    re_mathod(txt, n)









