import requests
import re
import time
from bs4 import BeautifulSoup
from attr import attrs, attrib
from fake_useragent import UserAgent


@attrs
class BiLiBiLiVidoDownLoad(object):
    # 禁用服务器缓存
    headers = attrib(default={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                            'AppleWebKit/537.36 (KHTML, like Gecko) '
                                            'Chrome/77.0.3865.90 Safari/537.36',
                              'Referer': 'https://www.bilibili.com/video/av69033665',
                              'Origin': 'https://www.bilibili.com'})
    target_url = attrib(default='https://www.bilibili.com/video/av69033665')  # 实验用url
    data_file_path = attrib(default=r'C:\Users\10248\Desktop\bili.txt')

    def save_url_data(self):
        with open(self.data_file_path, 'w', encoding='utf-8') as f:
            f.write(requests.get(self.target_url, headers=self.headers).text)

    def get_url_data(self):
        soup = BeautifulSoup(requests.get(self.target_url, headers=self.headers).text, 'lxml')
        soup1 = str(soup.find_all('script')[1])
        print(soup1)
        text = soup1.replace('"', '')
        p1 = re.compile(r'baseUrl:(.+?),')
        p2 = re.compile(r'bandwidth:(\d+?),')
        data = re.findall(p1, text)
        big = re.findall(p2, text)
        print(big)
        print(data)
        return data, big


    def get_mp4_url(self):
        url_list, file_big = self.get_url_data()
        headers = self.headers
        n_big = 0
        with open(r'C:\Users\10248\Desktop\bil.mp4', 'wb') as f:
            for i in range(len(url_list)):
                print('1')
                n_big += int(file_big[i])
                headers = {**headers, 'Range': f'bytes=0-920'}

                mp4_data = requests.get(url_list[i], headers=headers)
                print(mp4_data.status_code)
                f.write(mp4_data.content)
                time.sleep(1)



if __name__ == '__main__':
    b = BiLiBiLiVidoDownLoad()
    #b.get_mp4_url()
    b.save_url_data()
    b.get_url_data()








