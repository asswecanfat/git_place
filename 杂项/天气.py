import requests
from bs4 import BeautifulSoup

def get_url(url):#获取网页信息
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    reponse = requests.get(url, headers = headers)
    url_data = reponse.content
    return  url_data

def get_data(url_data):#获取txt
    with open('C:\\Users\\10248\\Desktop\\天气1.txt', 'wb') as f:
        f.write(url_data)

def get_web_data(url_data):#获取txt
    with open('C:\\Users\\10248\\Desktop\\天气2.txt', 'wb') as f:
        f.write(url_data)

def get_city(url_data):#获取文件中的城市
    soup = BeautifulSoup(url_data, 'html.parser')
    soup1 = soup.find_all('a')
    city = []
    city_p = []
    for i in range(len(soup1)):
        city_p.append(soup1[i]['href'])
        city.append(soup1[i].string)
    return city, city_p

def get_web(data_city):#获取城市的网页
    city_web = 'http://www.tianqi.com' + data_city
    city_data = get_url(city_web)
    return city_data

def get_city_konqi(city_data):
    soup = BeautifulSoup(city_data, 'html.parser')
    soup1 = soup.find_all('p', class_ = 'now')
    soup2 = soup.find_all('dd', class_ = 'shidu')
    soup3 = soup.find_all('dd', class_ = 'kongqi')
    print(soup1[0].get_text())
    text = ''
    for x in range(0,3):
        g = lambda x: soup2[0].find_all('b')[x].string
        text = text + str(g(x)) + ' '
    print(text)
    print(soup3[0].find('h5').string + ' ' + soup3[0].find('h6').string + ' ' + soup3[0].find('span').get_text())



url_data = get_url('http://www.tianqi.com/chinacity.html')
hot_city = []
hot_city_p = []
city, city_p = get_city(url_data)
for i in range(2, 36):
    hot_city.append(city[i])
    hot_city_p.append(city_p[i])
city_name = input('请输入城市:')
city_data = get_web(hot_city_p[hot_city.index(city_name)])
get_city_konqi(city_data)









