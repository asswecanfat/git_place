import requests
from bs4 import BeautifulSoup
import re

class Douban_login:
    def login(self):
        def post_data(data):#发送data并判断是否登陆成功
            reponse = s.post(url, data = data, headers = headers)
            if str(reponse.url) == final_url:
                print('登陆成功！')
            else:
                print('登陆失败，请再次重试！！')
            soup = BeautifulSoup(reponse.text, 'html.parser')
            soup1 = soup.find_all('span')
            user_name = soup1[0].string.replace('的帐号', '')
            print('登陆的账号为:' + user_name)
            

        def get_txt(url_data_text):#获取网页源文件
            with open('C:\\Users\\10248\\Desktop\\url_data.txt', 'w', encoding = 'utf-8') as f:
                f.write(url_data_text)

        def get_pit(pit_url):#获取验证码
            pit_data = s.get(pit_url)
            with open('C:\\Users\\10248\\Desktop\\yzm.jpg', 'wb') as f:
                f.write(pit_data.content)
            

        def get_url_data(url):#获取页面数据
            url_data = s.get(url, headers = headers)
            return url_data.text

        def deal_url_data(url_data_text):#处理网页并找出和下载验证码
            global yzm
            soup = BeautifulSoup(url_data_text, 'html.parser')
            soup1 = soup.find_all('img', id = 'captcha_image')
            if int(len(soup1)) == 0:
                yzm = 0
                print('无需验证码')
            else:
                yzm = 1
                pit_url = soup1[0].get('src')
                get_pit(pit_url)
                return pit_url

        def get_data(pit_url):#处理captcha:id并放入data中
            if yzm == 0:
                data={
                    'source' : 'index_nav',
                    'form_email' : user_ac,
                    'form_password' : user_password,
                    'user_login' : '登录'
                    }
                return data
            else:
                p = r'.+id=(.+)&size=s'
                data_list = re.findall(p, pit_url)#列表
                data = {
                    'source' : 'index_nav',
                    'form_email' : user_ac,
                    'form_password' : user_password,
                    'captcha-solution' : user_getin,
                    'captcha-id' : data_list[0],
                    'user_login' : '登录'
                    }
                return data
            

        url = 'https://www.douban.com/accounts/login'
        final_url = 'https://www.douban.com/'
        user_ac = str(input('请输入账号：'))
        user_password = str(input('请输入密码：'))
        s = requests.Session()
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',\
                  'Referer':'https://www.douban.com/'}
        url_data_text = get_url_data(url)
        pit_url = deal_url_data(url_data_text)
        if yzm == 1:
            user_getin = str(input('请输入验证码：'))
        data = get_data(pit_url)
        post_data(data)

