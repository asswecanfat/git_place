import requests
import urllib3
import re
import time
import random
import pymongo
from bs4 import BeautifulSoup
from attr import attrs, attrib
# TODO 还有验证删除

'''
主类IpPool,用于维护代理ip池
'''
@attrs
class IpPool(object):
    headers = attrib(default={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome'
                                                  '/76.0.3809.100 Safari/537.36'})
    catch_target_url = attrib(default='https://www.kuaidaili.com/free/inha/')

    def connect_db(self):
        """
        构建变量client用于连接数据库
        """
        client = None
        try:
            client = pymongo.MongoClient(host='localhost', port=27017)  # 连接数据库
            # dataBsae = client['Ip_Pool']  # 创建名为Ip_Pool的数据库
            connect_flag = True
        except:
            print('数据库连接错误！')
        finally:
            return client

    @staticmethod
    def test_ip(proxies: dict, url: str) -> int:
        try:
            code = requests.get(url, headers=IpPool.headers, proxies=proxies, verify=False, timeout=5).status_code
        except (TimeoutError,
                urllib3.exceptions.NewConnectionError,
                urllib3.exceptions.MaxRetryError,
                requests.exceptions.ProxyError):
            code = 0
        return code

    def __catch_ip(self):
        client = self.connect_db()
        url_page_num = self.__get_page_num()
        if 'Ip_Pool' not in client.list_database_names():
            mydb = client['Ip_pool']
        if 'pool' not in client['Ip_Pool'].list_collection_names():
            mycol = client['Ip_Pool']['pool']
        for i in range(1, url_page_num + 1):
            client['Ip_Pool']['pool'].insert_many(self.__get_ip(f'{self.catch_target_url}{i}', i))
            time.sleep(random.randint(1, 2))
            print(f'第{i + 1}页写入完成！')


    @staticmethod
    def init_dict():
        new_dict = {
            'IP': None,
            'PORT' : None,
            '匿名度': None,
            '类型': None,
            '位置': None,
            '响应速度': None,
            '最后验证时间': None,
        }
        return new_dict

    def __get_ip(self, url, page_num):
        dict_list = []
        text = requests.get(url, headers=self.headers).text
        soup = BeautifulSoup(text, 'lxml')
        deal = soup.find_all('td')
        new_dict = IpPool.init_dict()
        for num, data in enumerate(deal):
            if (num + 1) % 7 == 0:
                new_dict[data['data-title']] = data.text
                new_dict['_id'] = f'{page_num}_{num + 1}'
                dict_list.append(new_dict)
                new_dict = IpPool.init_dict()
            else:
                new_dict[data['data-title']] = data.text
        return dict_list

    def __get_page_num(self):
        text = requests.get(f'{self.catch_target_url}{1}', headers=self.headers)
        if text.status_code == 200:
            soup = BeautifulSoup(text.text, 'lxml')
            deal = soup.find_all('div', id="listnav")
            num_list = re.findall(r'\d+', str(deal[0]), re.M)
            return int(num_list[-1])
        else:
            return 0

    def run(self):
        self.__catch_ip()


if __name__ == '__main__':
    c = IpPool()
    c.run()
