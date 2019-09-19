from anime_catch import *


if __name__ == "__main__":
    test = CatChAniMe()
    rep = test.get_web_data(test.next_web)
    # test.save_root_web_data(rep)
    dic = test.deal_web_data(rep)
    # print(dic)
    test.download_anime(dic)
    # test.save_next_web_data(test.get_web_data(dict['第1话']))
