#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as bs
import requests
import traceback
import time
import os

# def test():
#     driver=webdriver.Chrome()
#     driver.get('https://hs.blizzard.cn/cards/')
#     time.sleep(5)
#     driver.quit()
#
# def nameTest():
#     str1='DRUID__UNG_116_zhCN_JungleGiants.png'
#     print(str1.split('_'))
#
# if __name__ == '__main__':
#     nameTest()
str1='DRUID__UNG_116_zhCN_JungleGiants.png'
print(str1.split('_'))
print(str1.split('_')[0])

# r=requests.get('https://hs.blizzard.cn/cards/')
# r.encoding=r.apparent_encoding
# print(r.text)
# soup=bs(r.text,'lxml')
# #srcs=soup.find_all('img',{'class':'imgload'})
# srcs=soup.select('img[class="imgload"]')
# print(type(srcs))
# print(srcs)
# for i in range(srcs):
#     src=srcs[i]
#     print(src)