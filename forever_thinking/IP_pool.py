import requests
import urllib3
import pymongo
from attr import attrs, attrib


'''
主类IpPool,用于维护代理ip池
'''
@attrs
class IpPool(object):
    headers: dict = attrib(default={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome'
                                                  '/76.0.3809.100 Safari/537.36'})
    target_url: str = attrib(default='https://www.mh1234.com/comic/11309')
    catch_target_url: str = attrib(default='https://www.kuaidaili.com/free/inha/1/')

    def catch_ip(self):
        """
        构建变量client用于连接数据库
        """
        client = pymongo.MongoClient(host='localhost', port=27017)  # 连接数据库
        dataBsae = client['Ip_Pool']  # 创建名为Ip_Pool的数据库

    def test_ip(self, proxies: dict) -> int:
        try:
            code = requests.get(self.target_url, headers=self.headers, proxies=proxies, verify=False, timeout=5).status_code
        except (TimeoutError,
                urllib3.exceptions.NewConnectionError,
                urllib3.exceptions.MaxRetryError,
                requests.exceptions.ProxyError):
            code = -1
        return code


if __name__ == '__main__':
    c = IpPool()
    c.catch_ip()
