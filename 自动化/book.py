import requests
from bs4 import BeautifulSoup
import time
import random
from learn import time_sum


class DowloadBook(object):
    def __init__(self):
        self.all_cha_url = 'http://book.zongheng.com/showchapter/859025.html'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                                      'Chrome/77.0.3865.90 Safari/537.36'}
        self.url_data_file = r'.\text.txt'
        self.book_path = r'.'
        self.step = 40

    def __get_url_data(self):
        url_list = []
        title_list = []
        text = requests.get(self.all_cha_url, headers=self.headers).text
        soup = BeautifulSoup(text, 'lxml')
        deal = soup.find_all('li', class_='col-4')
        book_name = soup.find('div', class_='book-meta').h1.text
        # print(book_name.h1.text)
        for i in deal:
            url_list.append(i.a['href'])
            title_list.append(i.a['title'])
        return book_name, url_list, title_list

    def __get_text(self, url_list):
        for i in range(len(url_list)):
            yield requests.get(url_list[i], headers=self.headers).text
            print(f'第{i + 1}话下载完成！')
            time.sleep(random.randint(1, 2))

    def get_book(self):
        book_name, url_list, title_list = self.__get_url_data()
        text_itetor = self.__get_text(url_list)
        # self.__deal_text(next(text_itetor))
        with open(f'{self.book_path}\\{book_name}.txt', 'w', encoding='utf-8') as f:
            for num, data in enumerate(text_itetor):
                f.write('{}{}{}'.format(" " * 10, title_list[num], '\n'))
                f.write(self.__deal_text(data))

    def __deal_text(self, text):
        first_text = ''
        soup = BeautifulSoup(text, 'lxml')
        deal_1 = soup.find('div', class_='content', itemprop='acticleBody')
        deal_2 = deal_1.find_all('p')
        for i in deal_2:
            _text = i.text
            if self.step < len(i):
                _text = '{}{}{}'.format(i.text[:self.step], '\n', i.text[self.step:])
            first_text += '{}{}{}'.format('  ', _text, '\n')
        return first_text


    def __repr__(self):
        return f'DowloadBook()'


if __name__ == '__main__':
    d = DowloadBook()
    t = time_sum.TimeSum()
    with t:
        d.get_book()
