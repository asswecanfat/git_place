import urllib.request as urr

def don():
    respone = urr.urlopen("http://www.fishc.com")
    ass = respone.read()
    html = ass.decode('utf-8')

    with open('fishc_first_page.txt', 'w') as f:
        f.write(html)


    with open('fishc_first_page.txt', 'r') as f:
        print(f.read(300))



    

if __name__ == '__main__':
    don()

