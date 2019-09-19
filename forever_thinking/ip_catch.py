import io
import random
import time

import requests
from bs4 import BeautifulSoup

s = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/74.0.3729.169 Safari/537.36'}


def get_web_data(ip_url, ip_num):
    web_reponse = s.get(ip_url, headers=headers)
    return  deal_web_data(web_reponse.text, ip_num)


def deal_web_data(text, ip_num):
    soup = BeautifulSoup(text, 'lxml')
    ip = soup.find_all(attrs={'data-title': 'IP'})
    port = soup.find_all(attrs={'data-title': 'PORT'})
    position = soup.find_all(attrs={'data-title': '位置'})
    request_speed = soup.find_all(attrs={'data-title': '响应速度'})
    with open(r'C:\Users\10248\Desktop\test\ip.txt', 'a', encoding='utf-8') as g:
        for num in range(len(ip)):
            g.write(ip[num].string + '          ' +
                    port[num].string + '          ' +
                    position[num].string + '          ' +
                    request_speed[num].string + '\n')
            ip_num += 1
        return ip_num


def run(page_num, ip_num):
    for i in range(page_num):
        if ip_num <= 500:
            time_random = random.randint(1, 3)
            ip_url = 'https://www.kuaidaili.com/free/inha/' + str(i+1) + '/'
            ip_num = get_web_data(ip_url, ip_num)
            time.sleep(time_random)
        else:
            break
    print('获取成功！')
    return 1


def test_ip(goal_url):
    with open(r'C:\Users\10248\Desktop\test\ip.txt', 'r', encoding='utf-8') as f:
        i = 0
        try:
            with open(r'C:\Users\10248\Desktop\test\ip_can_use.txt', 'a', encoding='utf-8') as g:
                while i < 10:
                    one_line = str(f.readline())
                    data = one_line.split()
                    proxy = str(data[0]) + ':' + str(data[1])
                    proxies = {'http': 'http://' + proxy, 'https': 'https://' + proxy}
                    try:
                        s.get(goal_url, headers=headers, proxies=proxies, timeout=1)
                    except (requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout):
                        continue
                    g.write(one_line)
                    print('已确认')
                    i += 1
        except (io.UnsupportedOperation, IndexError):
            print('测试完毕')


if __name__ == '__main__':
    sure = 0
    ip_num = 0
    try:
        if not sure:
            page_num = int(input('请输入想要爬取的页数:'))
            sure = run(page_num, ip_num)
        test_ip('http://ddrk.me/')
    except ValueError:
        print('输入的值有误！')
