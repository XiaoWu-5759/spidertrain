#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from bs4 import BeautifulSoup as bs
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

def run():
    browser = webdriver.Firefox()
    try:
        browser.get('https://www.baidu.com')
        input = browser.find_element_by_id('kw')
        input.send_keys('Python')
        input.send_keys(Keys.ENTER)
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
        print(browser.current_url)
        print(browser.get_cookies())
        print(browser.page_source)
    finally:
        browser.close()

def main():
    # from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
    #
    # # Create a new instance of the Firefox driver
    # binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
    # driver = webdriver.Firefox(firefox_binary=binary)
    pass

def test1():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://www.douyu.com/directory/all')
    soup = bs(driver.page_source, 'lxml')
    tName = soup.find_all('span', {'class': 'dy-name ellipsis fl'}, recrusive=True)
    print(type(tName))
    # tname=tName[0].find_all('span', {'class': 'dy-name ellipsis fl'}, recrusive=True)
    # print(type(tname))
    lives = soup.find('div', {'id': 'live-list-content'})
    print(type(lives))
    print(type(soup))
    # print(lives)
    # print(bs(str(lives), 'lxml').prettify())
    # print(type(bs(str(lives), 'lxml')))
    # names = lives.select("span[class='dy-name ellipsis fl']")
    # print(type(names))
    # print(names)
    # numbers = lives.select("span[class='dy-num fr']")
    # names = bs(str(lives), 'lxml').find_all('span', {'class': 'dy-name ellipsis fl'}, recrusive=True)
    # print(type(names))
    # numbers = bs(str(lives), 'lxml').find_all('span', {'class': 'dy-num fr'}, recrusive=True)
    # 还原键值对,赋值到字典中
    # 字典不好存储
    # for i in range(len(names)):
    #     name = names[i].text
    #     number = numbers[i].text
    #     # douyuDict[name]=number
    #     print('房间名:' + name + '\t观众人数:' + number)
    end = soup.find_all('a', {'class': 'shark-pager-item'})
    print(end[-1])

def test2():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)
    driver.get("https://www.baidu.com")
    print(driver.page_source)
    driver.close()

def test3():
    options = Options()
    options.add_argument('-headless')
    driver = webdriver.Firefox(executable_path='./geckodriver', firefox_options=options)
    driver.get("https://www.qiushibaike.com/8hr/page/1/")
    print(driver.page_source)
    driver.close()

def test4():
    options = FirefoxOptions()
    options.add_argument('--headless')
    dr = webdriver.Firefox(firefox_options=options)
    dr.get("https://www.baidu.com")
    print(dr.current_url)
    dr.close()

def moveAndClick():
    driver = webdriver.Firefox()
    driver.get('https://www.douyu.com/directory/all')
    next = driver.find_element_by_class_name("shark-pager-next")
    # actions = ActionChains(driver)
    # actions.move_to_element(next).perform()
    ActionChainsDriver=ActionChains(driver).move_to_element(next)
    ActionChainsDriver.perform()
    print('nihao')
    time.sleep(5)
    #driver.find_element_by_class_name("shark-pager-next").click()
    #actions.click(next).perform()
    print('nihao')
    time.sleep(1)
    # actions.click(next)
    # driver.close()

def click():
    import time
    from selenium import webdriver
    from selenium.webdriver.common.action_chains import ActionChains
    driver = webdriver.Chrome()
    driver.get('http://cn.bing.com/')
    #driver.maximize_window()
    driver.find_element_by_id('sb_form_q').send_keys('python')
    searchButtonElement = driver.find_element_by_id('sb_form_go')
    # ActionChainsDriver = ActionChains(driver).click(searchButtonElement)
    # ActionChainsDriver.perform()   #此时我们不执行perform()
    # time.sleep(5)
    # ActionChains(driver).move_to_element(searchButtonElement).perform()
    # print('nihao')
    # time.sleep(5)
    ActionChains(driver).click(searchButtonElement).perform()
    print('点击')
    time.sleep(5)
    #driver.quit()
    #driver.close()

if __name__ == '__main__':
    click()



