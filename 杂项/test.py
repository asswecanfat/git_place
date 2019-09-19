import requests

def get_url():
    re = requests.get("https://www.bilibili.com/")
    return re.content

def deal_data(txt):
    with open('C:\\Users\\10248\\Desktop\\text.txt','wb') as f:
        f.write(txt)

txt = get_url()
deal_data(txt)