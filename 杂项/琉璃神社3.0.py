import requests
from bs4 import BeautifulSoup
import re
from tkinter import *
import time

def get_data():#获取种子,图片和标题
    new_url = pan_url()
    for n in range(len(new_url)):
        url_data = get_url(new_url[n])
        link, title, pit = inget_url(url_data)
        for l in range(len(link)):
            source_seed = re.search(r'(?<=>).?(\d|[a-zA-z])+(?=(</.+>))',get_url(link[l]))
            if '熟' in source_seed.group():
                ssg = source_seed.group().replace('熟', '')
                seed = "magnet:?xt=urn:btih:" + ssg
            elif '生' in source_seed.group():
                ssg = source_seed.group().replace('生', '')
                seed = "magnet:?xt=urn:btih:" + ssg
            else:
                seed = "magnet:?xt=urn:btih:" + source_seed.group()
            
            if int(len(source_seed.group())) > 10:
                file_name = 'C:\\Users\\10248\\Desktop\\琉璃神社专用\\合集.txt'
                pit_address = 'C:\\Users\\10248\\Desktop\\琉璃神社专用\\' 
                with open(file_name, 'a', encoding='utf-8') as f:
                    f.write('第' + str(n+1)+ '页-' +str(l+1)+'.'+ seed + '  '+ title[l] + '\n')
                with open(pit_address + '第' + str(n+1) + '页-' + str(l+1) + '.jpg', 'wb') as g:
                    g.write(requests.get(pit[l]).content)
        time.sleep(0.5)
    print(str(len(new_url)) + '页全都获取完成!')

def pan_url():#通过标签判断网页
    new_url = []
    if str(e1.get()) == '动漫':
        for i in range(int(e2.get())):
            new_url.append('http://www.llss.lol/wp/category/all/anime/page/'+str(i+1) +'/')
        return new_url
    else:
        for i in range(int(e2.get())):
            new_url.append('http://www.llss.lol/wp/category/all/comic/page/'+str(i+1) +'/')
        return new_url
      
def get_url(new_url):#获取网页信息
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'}
    getUrl = requests.get(new_url, headers=headers)
    url_data = getUrl.text
    return url_data

def inget_url(url_data):#url_data):#获取一页中含有的url,文字,图片地址
    link = []
    title = []
    pit = []
    soup = BeautifulSoup(url_data, 'html.parser')
    soup1 = soup.find_all('h1',class_='entry-title' )
    soup2 = soup.find_all('img', alt='')
    for i in soup1:
        link.append(i.a['href'])
        title.append(i.a.text)
    for a in range(4,13):
        pit.append(soup2[a]['src'])
    return link, title, pit
        

tk = Tk()

Label(tk, text = '标签(动漫或漫画)：').grid(row=0, column=0,sticky = E,padx = 10, pady = 10)
e1 = Entry(tk)
e1.grid(row=0,column=1, padx = 10, pady = 10)
Label(tk, text = '页数：').grid(row=1, column=0,sticky = E,padx = 10, pady = 10)
e2 = Entry(tk)
e2.grid(row=1,column=1, padx = 10, pady = 10)
Button(tk, text='获取', command=get_data).grid(row=2, column=0,sticky=E, padx = 10, pady = 10)
Button(tk, text='退出', command=tk.quit).grid(row=2, column=1,sticky=E, padx = 10, pady = 10)


mainloop()


