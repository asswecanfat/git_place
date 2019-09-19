import selenium
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

browser = selenium.webdriver.Chrome()
browser.get('http://www.bilibili.com')#http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable
inp = browser.find_element_by_class_name('search-keyword')
inp.send_keys('mea')
inp.send_keys(Keys.ENTER)
window = browser.window_handles
time.sleep(2)
browser.switch_to.window(window[-1])#切换窗口
key = browser.find_elements_by_xpath('//li[@class="sub"]')
for i in range(len(key)):
    if key[i].text == '相簿':
        break
key[i].click()

photo = browser.find_elements_by_css_selector('[class="headline clearfix"]')
for j in photo:
    print(j.text)





