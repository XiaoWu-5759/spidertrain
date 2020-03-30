# 图片爬取全代码
import os

import requests

# r=requests.get("http://www.baidu.com")
# print(r.status_code)
# r.encoding = 'utf-8'
# print(r.text)
# 爬虫通用框架
# def getHtmlText(url):
#     try:
#         r=requests.get(url,timeout=30)
#         r.raise_for_status()  #如果状态不是200，引发HTTPError异常
#         r.encoding=r.apparent_encoding
#         return r.text
#     except:
#         return "产生异常"
#
# if __name__=="__main__":
#     url="http://www.baidu.com"
#     print(getHtmlText(url))
# HTTP协议对资源的六种操作
# get,head,post,put,patch,delete,OPTIONS
# 通过url来定位资源的位置
# 字典提交内容
# payload={'key1':'value1','key2':'value2'}
# r=requests.post('http://httpbin.org/post',data=payload)
# print(r.text)
# 控制访问的参数,json,13,params,data
# 京东商品页面的爬取
# url="https://item.jd.com/6733026.html"
# try:
#     r=requests.get(url)
#     r.raise_for_status()
#     r.encoding=r.apparent_encoding
#     print(r.text[:1000])
# except:
#     print("爬取失败")
# 修饰访问头文件
# https://www.amazon.cn/dp/B0186FESGW/ref=sa_menu_kindle_l3_ki
# url="https://www.amazon.cn/dp/B0186FESGW/ref=sa_menu_kindle_l3_ki"
# try:
#     kv={'user-agent':'Mozilla/5.0'}
#     r=requests.get(url,headers=kv)  #修改访问权限
#     # r=requests.get(url)
#     r.raise_for_status()
#     r.encoding=r.apparent_encoding
#     print(r.text[:1000])
# except:
#     print("爬取失败")
# 百度关键词接口：
# http://www.baidu.com/s?wd=keyword
# 360关键词接口：
# http://www.so.com/s?q=keyword
# keyword="Python"
# try:
#     kv = {'wd': 'Python'}
#     #kv1 = {'user-agent': 'Mozilla/5.0'}
#     r = requests.get("http://www.baidu.com/s",params=kv)
#     print(r.request.url)
#     r.raise_for_status()
#     print(len(r.text))
# except:
#     print("爬取失败")

url = "http://hearthstone.nos.netease.com/1/hscards/DRUID__UNG_116_zhCN_JungleGiants.png"
# root="/home/xiaowu/bear/"
# root="/files/hearthstone/"  #爬取失败
# root="/home/xiaowu/bear/hearthstone/"
root = ".\\xiaowu\\hearthstone"  # 此时必须要使用转义？
path = root + '\\' + url.split('/')[-1]
# 创建目录则可以先用getcwd取得当前目录之后再拼接目录名称即可创建文件夹了。
# 如果想要创建多级目录则要用到os模块中的makedirs才行唷。
# 而Python中用来删除文件夹则是用到os中的rmdir(只可以删除空滴文件夹)。
# 想要删除包含有内容的文件夹则必须引入shutil模块。然后再调用shutil模块的rmtree方法便可以删除文件夹了唷。

# 所谓绝对路径，是指从根目录算起来的路径。
# 所谓相对路径，是指相对于当前工作目录来说的，当前工作目录就是指的程序锁在的目录。
# 一般用.表示当前目录，用..表示父目录。
# try:
#     if not os.path.exists(root):
#         os.makedirs(root)
#     if not os.path.exists(path):
#         r = requests.get(url)
#         with open(path, 'wb') as f:
#             f.write(r.content)
#             f.close()
#             print("文件保存成功")
#     else:
#         print("文件已存在")
# except:
#     print("爬去失败")

# IP地址归属地的自动查询
# http://m.ip138.com/ip.asp?ip=ipaddress
# 只要是以更改url链接的方式都可以利用爬虫
# url="http://m,ip138,com/ip,asp?ip="
# try:
#     r=requests.get(url+'202.204.80.112')  #爬取失败，地址问题
#     r.raise_for_status()
#     r.encoding=r.apparent_encoding
#     print(r.text[-500:])
# except:
#     print("爬取失败")
