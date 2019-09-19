import requests

def get_url(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    reponse = requests.get(url,headers=headers)
    return reponse.content

def download(iamge,n):
    with open('C:\\Users\\10248\\Desktop\\EDA试卷(16)\\' + n + '.docx','wb') as f:
        f.write(iamge)


url = input('请输入图片网址：')
n = input('请输入图片名称:')
iamge = get_url(url)
download(iamge,n)