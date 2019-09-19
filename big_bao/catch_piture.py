import urllib.request as urr

def catch():
    string = input("请输入需要的图片的网址：")
    strin = urr.Request(string)
    respone = urr.urlopen(strin)
    bitch = respone.read()
    with open("one_piture.jpg", 'wb') as f:
        f.write(bitch)

if __name__ == '__main__':
    catch()
