import random
import re
import time

import requests
from attr import attrs, attrib
from bs4 import BeautifulSoup

from HACG_anime import SeedDealError, OverError, WebDealError, download_p, check_dict


def to_int(value):
    try:
        if 0 < int(value) < 5:
            return int(value)
        else:
            raise OverError('数字不在1~4范围内!')
    except ValueError:
        raise ValueError('该值需为数字！！')


@attrs
class HacgComicSprider(object):
    Hacg_class = '漫画'
    s = requests.Session()
    pattern = re.compile(r'[a-zA-Z0-9]{40}', re.S)
    proxy = attrib(default=None)
    headers = attrib(default={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                            'AppleWebKit/537.36 (KHTML, like Gecko) '
                                            'Chrome/74.0.3729.169 Safari/537.36'})
    comic_page = attrib(kw_only=True, default=1, converter=to_int)

    def get_url_data(self):
        if self.proxy is None:
            proxies = None
        else:
            proxies = {'http': 'http://' + self.proxy, 'https': 'https://' + self.proxy}
        for i in range(1, self.comic_page):
            now_url = 'http://llss.pl/wp/category/all/comic/page/' + str(i) + '/'
            reponse = self.s.get(now_url, headers=self.headers, proxies=proxies)
            p_s_u = self.__deal_web_data(reponse.text, i)
            download_p(HacgComicSprider, p_s_u)
            sure = check_dict(p_s_u)
            if not sure:
                raise SeedDealError('种子解析出错！')

    def __deal_web_data(self, data, web_page):
        p_string_url = {}
        soup = BeautifulSoup(data, 'lxml')
        p_url_data = soup.find_all(name='div', class_='entry-content')  # 首页第一个不是
        string_data = soup.find_all(name='h1', class_="entry-title")
        if len(p_url_data[1:]) != len(string_data) and web_page == 1:
            raise WebDealError('网页结构有变化！')
        else:
            pass
            if web_page == 1:
                for i in range(len(string_data)):
                    result = self.__get_seed(p_url_data[i + 1].a['href'])
                    p_string_url[p_url_data[i + 1].img['src']] = [string_data[i].a.string,
                                                                  p_url_data[i + 1].a['href'],
                                                                  result]
                    time.sleep(random.randint(1, 2))
            else:
                for i in range(len(string_data)):
                    result = self.__get_seed(p_url_data[i].a['href'])
                    p_string_url[p_url_data[i].img['src']] = [string_data[i].a.string,
                                                              p_url_data[i].a['href'],
                                                              result]
                    time.sleep(random.randint(1, 2))
        return p_string_url

    def __get_seed(self, url):
        if self.proxy is None:
            proxies = None
        else:
            proxies = {'http': 'http://' + self.proxy, 'https': 'https://' + self.proxy}
        reponse = self.s.get(url, headers=self.headers, proxies=proxies)
        with open(r'C:\Users\10248\Desktop\test\Hacg_漫画种子.txt', 'w', encoding='utf-8') as f:
            f.write(reponse.text)
        results = re.findall(self.pattern, reponse.text)
        return results


if __name__ == '__main__':
    hc = HacgComicSprider()
    hc.get_url_data()
