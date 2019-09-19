import requests
from bs4 import BeautifulSoup
import http.cookiejar
import re

def fuck_t(string):#删除'\t'
    while True:
        if '\t' in string:
            string = string.replace('\t', '')
        else:
            break
    return string
    

def get_url():#获取网页信息
    a = s.get('http://authserver.gdut.edu.cn/authserver/login?service=http%3A%2F%2Fjxfw.gdut.edu.cn%2Fnew%2FssoLogin')
    return a.text

def deal_masurl(respone):#传入网页信息并处理
    soup = BeautifulSoup(respone, 'html.parser')
    a = soup.find_all('input')
    return a[2]['value']

def put_data(value, ac, pa):#放置数据
    data = {
    'username':ac,
    'password':pa,
    'lt':value,
    'dllt':'userNamePasswordLogin',
    'execution':'e1s1',
    '_eventId':'submit',
    'rmShown':'1'
    }
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    return data,headers

def post_data(data,headers):#传入数据
    a = s.post('http://authserver.gdut.edu.cn/authserver/login?service=http%3A%2F%2Fjxfw.gdut.edu.cn%2Fnew%2FssoLogin', data=data, headers=headers)
    return a.url

s=requests.Session()
s.cookies=http.cookiejar.CookieJar()#保持回话
a = get_url()
b = deal_masurl(a)
ass = str(input('请输入账号：'))
can = str(input('请输入密码：'))
c, d = put_data(b, ass, can)
e = str(post_data(c,d))
if e == 'http://jxfw.gdut.edu.cn/login!welcome.action':
    print('登陆成功！')
    sea = s.get('http://jxfw.gdut.edu.cn/login!welcome.action')
    bea = BeautifulSoup(sea.text, 'html.parser')
    baa = bea.div
    cnno = baa.get_text()
    p = r'(.+)'
    se = re.findall(p, cnno)
    se[1] = fuck_t(se[1])
    se[11] = fuck_t(se[11])
    print('登陆的用户为：'+se[1])
    print(se[11])
else:
    print('登陆失败！')
