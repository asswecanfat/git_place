import requests
from bs4 import BeautifulSoup

url = 'https://store.steampowered.com/'

def get_url_data(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    reponse = requests.get(url, headers=headers)
    return reponse


def save_as_file(reponse):
    with open(r'C:\Users\10248\Desktop\steam.txt', 'wb') as f:
        f.write(reponse.content)

def deal_data(reponse):
    soure_data = reponse.text
    soup = BeautifulSoup(soure_data, 'lxml')
    main = soup.find_all(class_='home_tabs_content')
    game_name = main[0].find_all(class_='tab_item_name')
    game_money = main[0].find_all(class_='discount_final_price')
    print(game_money)
    print(game_name)

data = get_url_data(url)
# save_as_file(data)
deal_data(data)