import requests
from attr import attrs, attrib


@attrs
class BiliBili(object):
    target_utl = attrib(default='https://t.bilibili.com')
    data_save_path = attrib(default=r'C:\Users\10248\Desktop\test.txt')
    headers = attrib(default={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                            'AppleWebKit/537.36 '
                                            '(KHTML, like Gecko)'})

    def save_ul_data(self):
        with open(self.data_save_path, 'wb') as f:
            f.write(requests.get(self.target_utl, headers=self.headers).content)



if __name__ == '__main__':
    b = BiliBili()
    b.save_ul_data()
