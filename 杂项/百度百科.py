import requests
from bs4 import BeautifulSoup

def get_url_data(url,key):#获取网页信息
    real_url = url + key
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    reponse = requests.get(real_url, headers = headers)
    return reponse.content

def file_data(data):#保存为文件
    with open('C:\\Users\\10248\\Desktop\\1.txt', 'wb') as f:
        f.write(data)

def deal_data(data):#处理网页数据
    soup = BeautifulSoup(data, 'lxml')
    soup1 = soup.find_all('meta')
    need_data = soup1[3]['content'].replace('.','')
    print(need_data)

key = input('请输入要搜索的关键字;')
url = 'https://baike.baidu.com/item/'
data = get_url_data(url, key)
deal_data(data)
