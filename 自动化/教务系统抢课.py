from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
from selenium.webdriver.support.select import Select

account = input('请输入学号：')#'3117004627'
password = input('请输入密码：')#'99271727f'
try:
    target_url = 'http://jxfw.gdut.edu.cn/login!welcome.action'#http://www.jxfw.gdut.edu.cn/login!welcome.action
    browser = webdriver.Chrome()
    browser.get(target_url)
    input_account = browser.find_element_by_id('account')
    input_password = browser.find_element_by_id('password')
    input_id_code = browser.find_element_by_id('j_captcha')
    input_account.send_keys(account)
    input_password.send_keys(password)
    input_id_code.click()
    time.sleep(1)
    browser.save_screenshot('C:\\Users\\10248\\Desktop\\id_code.png')
    id_code_real = input('请输入验证码：')
    input_id_code.send_keys(id_code_real)
    botton = browser.find_element_by_id('submit_btn')
    botton.click()
    time.sleep(1)
    select_btton = browser.find_element_by_id('sm2')
    select_btton.click()
    to_element = browser.find_element_by_css_selector("[class='combo-arrow']")
    to_element.click()
    time.sleep(1)
    to_element.find_element_by_link_text('个人选课').click()
    print(1)
finally:
    pass


