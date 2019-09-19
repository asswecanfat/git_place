import os
import random
import re
import sys
import time

import requests
from attr import attrs, attrib
from bs4 import BeautifulSoup


class OverError(Exception):  # 自定义错误类型，数字范围溢出
    pass


class SeedDealError(Exception):  # 自定义错误类型，种子解析错误
    pass


class WebDealError(Exception):  # 自定义错误类型，网页解析错误
    pass


def to_int(value):
    try:
        if 0 < int(value) < 5:
            return int(value)
        else:
            raise OverError('数字不在1~4范围内!')
    except ValueError:
        raise ValueError('该值需为数字！！')


@attrs
class HacgAnimeSprider(object):
    Hacg_class = '动漫'
    s = requests.Session()
    pattern = re.compile(r'[a-zA-Z0-9]{40}', re.S)
    proxy = attrib(default=None)
    headers = attrib(default={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                            'AppleWebKit/537.36 (KHTML, like Gecko) '
                                            'Chrome/74.0.3729.169 Safari/537.36'})
    anime_page = attrib(kw_only=True, default=1, converter=to_int)

    def get_url_data(self):
        if self.proxy is None:
            proxies = None
        else:
            proxies = {'http': 'http://' + self.proxy, 'https': 'https://' + self.proxy}
        for i in range(1, self.anime_page):
            now_url = 'http://llss.pl/wp/category/all/anime/page/' + str(i) + '/'
            reponse = self.s.get(now_url, headers=self.headers, proxies=proxies)
            p_s_u = self.__deal_web_data(reponse.text, i)
            download_p(HacgAnimeSprider, p_s_u)
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
        with open(r'C:\Users\10248\Desktop\test\Hacg_动画种子.txt', 'w', encoding='utf-8') as f:
            f.write(reponse.text)
        results = re.findall(self.pattern, reponse.text)
        return results


def check_dict(_dict):  # _dict储存结构key：[string, web_url, result]
    for value in _dict.values():
        if not len(value[2]):
            return 0


def download_p(_class, _dict):  # 后续扩展为自选路径
    if os.path.exists('C:\\Users\\10248\\Desktop\\琉璃神社\\' + _class.Hacg_class):
        d_p_other(_class, _dict)
    else:
        if os.path.exists(r'C:\Users\10248\Desktop\琉璃神社'):
            os.makedirs('C:\\Users\\10248\\Desktop\\琉璃神社\\' + _class.Hacg_class)
            d_p_other(_class, _dict)
        else:
            os.makedirs(r'C:\Users\10248\Desktop\琉璃神社')
            os.makedirs('C:\\Users\\10248\\Desktop\\琉璃神社\\' + _class.Hacg_class)
            d_p_other(_class, _dict)


def d_p_other(_class, _dict):
    if _class.proxy is None:
        proxies = None
    else:
        proxies = {'http': 'http://' + _class.proxy, 'https': 'https://' + _class.proxy}
    for pit_url, value in _dict.items():  # value为列表，里面顺序[string, web_url, result]
        reponse = _class.s.get(pit_url, headers=_class.headers, proxies=proxies)
        p_string = p_name = value[0]
        for r in value[2]:
            p_string += '  magnet:?xt=urn:btih:' + r  # windows文件名中允许使用空格，但不允许使用下列字符（英文输入法状态）：< > / \ | : " * ?；
        p_name = 'C:\\Users\\10248\\Desktop\\琉璃神社\\' + _class.Hacg_class + '\\' + p_name + '.jpg'
        with open(p_name, 'wb') as f:
            f.write(reponse.content)
        with open('C:\\Users\\10248\\Desktop\\琉璃神社\\' + _class.Hacg_class + '\\seed.txt', 'a', encoding='utf-8') as g:
            g.write(p_string + '\n')
        time.sleep(random.randint(1, 2))


if __name__ == '__main__':
    from HACG_comic import HacgComicSprider
    '''Python中可能会遇到 cannot import name ‘XXX’ 错误, 
    其实这有可能出现再模块导入的顺序问题上， 
    比如：在A文件头执行到语句 from B import XXX ，
    程序马上就会转到B文件中去，从头到尾顺序寻找B文件中的XXX函数，
    而A文件就暂停执行，直到把XXX函数复制到内存中，但B文件中的文件头可能也有导入， 
    如果B文件头中又导入了A文件中的函数，由于XXX函数还没有被复制。
    所以于A文件因为暂停执行而无法导入，就会出现上面的错误了。'''
    print('1.动漫')
    print('2.漫画')
    print('3.电子书')
    print('____________')
    print('0.退出')
    try:
        while 1:
            c_num = int(input('请输入序号：'))
            if c_num == 0:
                print('已退出~~~欢迎下次使用~~')
                sys.exit()
            page_num = input('请输入想要爬取的页数：')
            if c_num == 1:
                hs = HacgAnimeSprider(anime_page=page_num)
                hs.get_url_data()
            elif c_num == 2:
                hc = HacgComicSprider(comic_page=page_num)
                hc.get_url_data()
            elif c_num == 3:
                pass
                # hs = HacgSprider(chiose_num=c_num, book_page=page_num)
                # hs.get_url_data()
    except ValueError:
        print('该值需为数字！！')
    except OverError:
        print('输入的数字不在0~5范围内!')
    except SeedDealError:
        print('种子解析出错！')
    except WebDealError:
        print('网页结构有变化！')

    # hs.test()

def test():
    print('import yes')