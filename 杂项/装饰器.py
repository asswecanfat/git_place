import requests, time

def write_data(txt):
    print(txt.__name__)
    with open('C:\\Users\\10248\\Desktop\\1.txt','wb') as f:
        a,b = txt()
        f.write(a)
        print(time.time() - b)

@write_data
def get_url_data():
    logal = time.time()
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}
    reponse = requests.get('https://blog.csdn.net/u012759262/article/details/79749299',headers = headers)
    return reponse.content, logal


