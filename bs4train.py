import requests
from bs4 import BeautifulSoup

r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
# print(demo)
# 相关解析器，html，xml文件
soup = BeautifulSoup(demo, "html.parser")  # 坐上一锅soup
# print(soup.prettify())

# 标签Tag总是成对出现，属性定义标签的特点，字符串
# html文件和标签树、beautifulsoup类（变量），三者是等价的
# beautifulsoup一共有五中基本元素，Tag，Name，Attributes，NavigableString，Comment
# <tag>.name <tag>.attrs <tag>.string
# print(soup.title)
# tag=soup.a
# print(tag)
# print(soup.a.name)
# print(soup.a.parent.name)
# print(soup.a.parent.parent.name)
#
# print(tag.attrs)  #一个字典类型
# print(tag.attrs['class'])
# print(type(tag.attrs))
#
# print(soup.a.string)  #string跨越多个标签形式
# print(type(soup.p.string))
# 对注释部分通过type分析
# newsoup=BeautifulSoup("<b><!--This is a comment--></b><p>This is a comment</p>","html.parser")
# print(newsoup.b.string)
# print(type(newsoup.b.string))
# print(newsoup.p.string)
# print(type(newsoup.p.string))

# html内容的遍历方式，如何从一个节点跳到另一个节点
# 三种遍历方式，下行遍历，上行遍历，平行遍历
# 下行遍历.contents子节点列表，.children子节点的迭代类型，用于循环遍历儿子节点，
# .descendants子孙节点的迭代类型，包含所有的子孙节点，用于循环遍历
# print(soup.head)
# print(soup.head.contents)  #返回的时列表类型
# print(len(soup.body.contents))
# print(soup.body.contents[1])
# 通过循环遍历
# 遍历儿子节点
# for child in soup.body.children:  #返回的是迭代类型
#     print(child)
# 遍历子孙节点
# for child in soup.body.children:
#     print(child)
# 标签树的上行遍历
# .parent节点的父亲标签，.parents节点先辈标签的迭代类型，父亲的父亲的父亲
# 循环遍历上行代码
# for parent in soup.a.parents:
#     if parent is None:  #会遍历到soup本身
#         print(parent)
#     else:
#         print(parent.name)
# 标签树的平行遍历
# .next_sibling下一个平行节点标签,.previous_sibling上一个平行节点标签,
# 迭代类型.next_silings,.previous_siblings
# for sibling in soup.a.next_siblings:
#     print(sibling)
# for sibling in soup.a.previous_siblings:
#     print(sibling)

# 信息标记的三种方式,和信息一样重要
# 标记后的信息可用于通信.存储或展示;标记后的信息有利于程序的理解和运用
# 国际公认的信息标记形式:xml.json(有类型的键值对,双引号变成字符串,有数值类型的键值对,方括号加逗号).
# "key":[value1,value2]
# yaml无类型的键值对,仅有字符串,利用缩进,减号表达并列关系 |表达整块数据,# 表示注释
# internet用xml,json无注释,适合程序,接口传输,yaml各类系统的配置文件,有注释易读
# 信息提取,1.标记解析器,遍历2.直接搜索,查找
# 结合形式解析与搜索方法,提取关键信息,需要同时有标记解析器和文本查找函数

# 查找a标签
# for link in soup('a'):
#     print(link.get('href'))
# find_all参数有name,attrs,
# recursive是否针对子孙节点的值,string,**kwargs
# find_all(['a','b'])  # 返回列表类型
# for tag in soup.find_all(re.compile('b')):
#     print(tag.name)
# soup.find_all(id=re.compile('link'))
# 简写,直接在括号()里写

# 中国大学排名定向爬虫(不扩展爬虫,只有一个url)
# 中国大学最好网
# http://www.zuihaodaxue.com/zuihaodaxuepaiming2017.html
# 程序结构设计,封装模块,提高可读性
# step1:从网络上获取大学排名网页内容 getHTMLText()
# step2:提取网页内容中信息到合适的数据结构 fillUnivList()
# step3:利用数据结构展示并输出结果 printUnivList()


# 测试
# soup1=BeautifulSoup('<a href="http://quote.eastmoney.com/sh201000.html" target="_blank">R003(201000)</a>',"html.parser")
# a=soup1.find('a')
# print(type(a))
# print(a.attrs)
# href=a.attrs['href']
# print(href)

# soup2=BeautifulSoup('<a name="sh"></a>',"html.parser")
# a=soup2.find('a')
# href=a.attrs['href']  #就是有误报错
# print(type(href))
