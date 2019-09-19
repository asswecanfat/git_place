import requests
from bs4 import BeautifulSoup

def req():#维持通话
    s = requests.Session()
    return s

def get_url(url,s):#获取URL的内容
    reponse = s.get(url)
    return reponse.content

def save_data(url_data):#将网页保存为文件
    with open('C:\\Users\\10248\\Desktop\\1.txt','wb') as f:
        f.write(url_data)

def deal_data(url_data):#处理It数据
    soup = BeautifulSoup(url_data, 'lxml')
    soup1 = soup.find_all('input', type="hidden")
    lt = soup1[1]['value']
    execution = soup1[2]['value']
    return lt,execution

def login(lt, execution, s):
    data = {'lt':lt, 'username':'15521318232', 'password':'99271727faa', 'execution':execution, '_eventId':'submit', 'iframe':'false', 'fkid':'WHJMrwNw1k/Gs4yCuLqh9sNl7OLr2qbVegbI05dYIAUm4XzFzfWCPP4/LWuHVaWN230moR170pfxctPMBoFRWgoLy6c+ECjdqxNLrnR5uWfl7OdP6HJZDZw/GllaqVP3BvWdC0QQex8haJKwy8P/vgNzza0a/kPEfye4BouPtlUauOX53ZfF9WJSQLpaPG7pfO4MXRnOZiUTNtAKvckCXnwgKnXCd7i6b00mILJTmM0KVk9VxcBFcuNwuOXG+4ocFQ2C5nbwxLKYXXT+s9g2g3A==1487582755342'}
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    reponse = s.post('https://passport.csdn.net/account/verify', data = data, headers = headers)
    print(reponse.url)
    print(data)

login_url = 'https://passport.csdn.net/account/login'
s = req()
url_data = get_url(login_url,s)
save_data(url_data)
lt,execution = deal_data(url_data)
login(lt, execution,s)