import requests
import threading
import re
from time import sleep
import random
from bs4 import BeautifulSoup


class CatChAniMe(object):

    def __init__(self):
        self.root_web: str = "https://www.mh1234.com"  # https://www.mh1234.com/comic/11309
        self.next_web: str = "https://www.mh1234.com/comic/11309"
        self.hide_head: str = 'https://mhpic.dongzaojiage.com'  # 图片所需头部
        self.headers: dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome'
                                            '/76.0.3809.100 Safari/537.36'}
        self.save_data_path: str = r'C:\Users\10248\Desktop'  # 数据保存位置
        self.save_anime_path: str = r'C:\Users\10248\Desktop\anime'  # 漫画保存位置

    def get_web_data(self, web: str) -> requests:
        requests.packages.urllib3.disable_warnings()
        return requests.get(web, headers=self.headers, verify=False)

    def save_root_web_data(self, rep: requests):
        with open('{}{}'.format(self.save_anime_path, r'\ainme.txt'), 'wb') as f:
            f.write(rep.content)

    def save_next_web_data(self, rep: requests):
        with open('{}{}'.format(self.save_anime_path, r'\ainme_next.txt'), 'wb') as f:
            f.write(rep.content)

    def deal_web_data(self, rep: requests) -> dict:
        data_saver = {}
        soup = BeautifulSoup(rep.content, 'lxml')
        deal1 = soup.find_all('ul', id='chapter-list-1')
        deal2 = deal1[0].find_all('a')
        for i in deal2:
            data_saver[i.text] = '{}{}'.format(self.root_web, i['href'])
        return data_saver

    def __deal_anime(self, url: str, head: str):
        reponse = requests.get(url, headers=self.headers)
        pattern = re.compile(r'\["(.+)\"]')
        deal_fc = pattern.findall(reponse.text)
        final_data = re.sub(r'(\\)|"', '', deal_fc[0]).split(',')
        for i, jpg in enumerate(final_data):
            file_name = '{}{}'.format('\\', head + '_' + str(i) + '.jpg')
            with open('{}{}'.format(self.save_anime_path, file_name), 'wb') as f:
                f.write(requests.get('{}{}'.format(self.hide_head, jpg), headers=self.headers).content)
            sleep(random.uniform(0, 0.5))

    def download_anime(self, ds: dict):
        thread = []
        self.__deal_anime(ds['第1话'], '第1话')
        for head in list(ds.keys()):
            t = threading.Thread(target=self.__deal_anime, args=(ds.pop(head), head), name=head)
            thread.append(t)
            t.start()
            time.sleep(1)
        for i in thread:
            i.join()
        print('\n全部完成！！')
