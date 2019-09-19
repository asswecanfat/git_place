from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://www.bilibili.com')#http://www.python.org
input_ = browser.find_element_by_class_name('search-keyword')
input_.send_keys('鸡你太美')
input_.send_keys(Keys.ENTER)