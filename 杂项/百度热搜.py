import requests
from bs4 import BeautifulSoup

def get_url_data(url):#获取网页数据
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    reponse = requests.get(url, headers = headers)
    return reponse.content

def deal_url_data(byte_data):#用美丽汤处理文本
    soup = BeautifulSoup(byte_data, 'lxml')
    soup1 = soup.find_all('table', class_="c-table opr-toplist1-table")
    soup2 = soup1[0].find_all('a', target="_blank")
    soup3 = soup1[0].find_all('td', class_="opr-toplist1-right")
    for i in range(len(soup2)):
        print(str(i+1) + '.' + soup2[i].string + ' ' + soup3[i].text)


url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=%E6%8C%89%E6%97%B6&rsv_pq=cdf9649a0000a7ca&rsv_t=8a2c4MPWQ8TfqgPcYbPtieaKRshfRaBPxdW5dTlulEigBNgurRVEyaaTNPs&rqlang=cn&rsv_enter=0&rsv_sug3=3&rsv_sug1=3&rsv_sug7=100&inputT=2580&rsv_sug4=2580'
byte_data = get_url_data(url)
deal_url_data(byte_data)
