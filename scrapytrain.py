# 功能强大的网络爬虫框架
# 非常优秀的python第三方库,重要的技术路线
# scrapy-h 不是一个简单的库
# 是一个爬虫框架,是实现爬虫功能的一个软件结构和功能组件集合,是一个半成品,能够帮助用户实现专业网络爬虫
# scrapy 一共5+2结构,五个主要部分,engine,scheduler,item pipelines,spiders,downloader
# 中间件模块 spiders和engine engine和downloader,在结构之间流动,形成数据流

# 三条主要数据流
# spiders(响应,response)-engine-scheduler(进行调度)
# scheduler(request)-engine(request)-down(response)-engine(response)-spiders

# spiders(items/request)-engine(items)-item pipeline(爬取项)
#                                     -request(scheduler)(对新的链接继续爬取,进行调度)
# 配置,入口spider,出口item pipeline

# 各个部分的功能
# engine控制所有模块的数据流(核心,发动机)
# downloader(下载页面)
# scheduler(对所有爬取请求进行调度)
# Downloader Middleware
# 目的:实施engine,scheduler,downloader之间进行用户可配置的控制,功能:修改/丢弃/新增请求和响应
# spider 1.解析Downloader返回的响应(response) 2.产生爬取项(scraped item)
# 3.产生额外的爬取请求(Request) 用户主要编写的模块
# item pipeline 以流水线方式处理爬取项
# 由一组操作顺序组成,类似流水先,每个操作是一个item pipeline类型,可能操作包括
# 清理,检验和查重爬取项中的html数据,将数据存储到数据库中
# spider middleware
# 目的:对请求和爬取项在处理,功能:修改/丢弃/新增请求或爬取项

# request和scrapy都没有处理js\提交表单\应对验证码等功能(可扩展)
# Scrapy 是为了持续运行设计的专业爬虫框架,提供操作的scrapy命令行
# 常用命令
# startproject,genspider,setting(获取爬虫配置信息),crawl(运行),list(列出工程中所有爬虫)
# shell启动url调度命令 scrapy shell
# 一个工程有多个爬虫
# 为什么scrapy采用命令行创建和运行爬虫?
# 命令行(不是图形界面)更容易自动化,适合脚本控制
# 本质上,scrapy是给程序员用的,功能(而不是见面)更重要

# 建立一个scrapy工程
# scrapy 部署市场让朋友爬虫的配置文件
# __init__.py初始脚本,items.py Items代码模板(继承类)
# middleware.py middleware代码模板(继承类)
# pipelines.py pipelines代码模板(继承类)
# setting.py  scrapy爬虫的配置文件
# spider __init__.py 初始文件,无需修改,__pycache__/ 缓存目录,无需修改

# step1:建立一个scrapy爬虫工程
# step2:在工程中产生一个scrapy爬虫
# step3:配置产生的spider爬虫
# step4:运行爬虫,获取网页

# yield关键字
# yield与生成器
# 生成器是一个不断产生值的函数
# 包含yield语句的函数是一个生成器
# 生成器每次产生一个值(yield语*句),函数被冻结,被唤醒后再产生一个值
# def gen(n):
#     for i in range(n):
#         yield i**2
#
# for i in gen(5):  #返回一个值,循环返回
#     print(i,"",end="")

# 普通的写法,所有的值计算出来,再返回出来
# def square(n):
#     ls=[i**2 for i in range(n)]
#     return ls
#
# for i in square(5):
#     print(i,"",end="")

# 生成器相比一次列出所有内容的优势
# 更节省存储空间
# 响应更迅速
# 使用更灵活
# 如果n=1M或者更多呢

# Scrapy爬虫的使用步骤
# step1: 创建一个工程和spider模板
# step2: 编写Spider
# step3: 编写Item Pipeline
# step4: 优化配置策略

# Scrapy爬虫的数据类型
# Request类,一个请求对象,由spider生成,downloader执行
# .url,.method,.headers(字典类型风格的请求头),.body,.meta,.copy()
# Response类,一个http响应,由downloader生成,由spider执行
# .url,.status,.headers,.body,.flags,.request,.copy()
# Item类,表示一个从html页面中提取的信息内容,由spider生成,由item Pipeline处理,按照字典类型操作
# html信息提取方法,beautifulsoup,lxml,re,Xpath Selector,CSS Selector
# CSS Selector的基本使用
# <HTML>.css('a::attr(href)').extract()

# 股票数据爬取
# 优化,提高爬取的速度
# 配置并发连接选项
# concurrent_requests,downloader最大并发请求下载数量,默认32
# concurrent_items,Item Pipelines最大并发item处理数量,默认100
# concurrent_request_per_domain,每个目标域名最大的并发请求数量,默认8
# concurrent_request_per_ip,每个目标IP最大的并发请求数量,默认0,非0有效
