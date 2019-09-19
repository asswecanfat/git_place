import requests
from bs4 import BeautifulSoup
from attr import attrib, attrs
import json
import re
import random
import os


@attrs
class BiliBili(object):
    file_path = attrib(default=r'C:\Users\10248\Desktop\1.txt')
    pic_path = attrib(default=r'C:\Users\10248\Desktop')
    source_wab_url = attrib(default='https://search.bilibili.com/all?keyword=')
    headers = attrib(default={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                            'AppleWebKit/537.36 (KHTML, like Gecko) '
                                            'Chrome/75.0.3770.142 Safari/537.36'})

    def update_url(self, av_num):
        self.source_wab_url = '{}{}{}'.format(self.source_wab_url, av_num, '&from_source=banner_search')

    def get_url_data(self, url):
        return requests.get(url, headers=self.headers)  # reponse

    def download_cover(self):
        reponse = self.get_url_data(self.source_wab_url)
        self.source_wab_url.__init__()
        # self.test_save_data(reponse)
        pic_url = '{}{}'.format(' http:', self.deal_web_data(reponse))
        final_pic_path = r'{}\{}'.format(self.pic_path, str(random.randint(0, 1000)) + '.jpg')
        while os.path.exists(final_pic_path):
            final_pic_path = r'{}\{}'.format(self.pic_path, str(random.randint(0, 1000)) + '.jpg')
        with open(final_pic_path, 'wb') as f:
            f.write(self.get_url_data(pic_url).content)
        print('封面获取成功！')

    def deal_web_data(self, reponse):
        soup = BeautifulSoup(reponse.text, 'lxml')
        point = soup.find_all('script')
        # print(point[6])
        real_data = re.split(r'=|;\(', point[6].text)[1]
        # print(real_data)
        now = json.loads(real_data)
        # print(now['allData']['video'][0]['pic'])
        return now['allData']['video'][0]['pic']

    def test_save_data(self, reponse):
        with open(self.file_path, 'wb') as f:
            f.write(reponse.content)


if __name__ == '__main__':
    bi = BiliBili()
    av_n = input('请输入av号：')
    bi.update_url(av_n)
    bi.download_cover()
