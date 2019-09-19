import requests
from bs4 import BeautifulSoup

def get_url(news_url):#新闻页面获取
    url_source_data = requests.get(news_url)
    url_data = url_source_data.content
    return url_data

def deal_url_data(url_data):#用美丽汤
    soup = BeautifulSoup(url_data, 'html.parser')
    soup1 = soup.find_all('div',class_ = "ct_t_01")
    soup2 = soup1[0].find_all('a',target="_blank")
    print(soup2)




news_url = 'https://news.sina.com.cn/'
url_data = get_url(news_url)
deal_url_data(url_data)

