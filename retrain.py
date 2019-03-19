# 正则表达式
# 用来简洁表达一组字符串的表达式,需要一个编译过程
# 简洁,表达字符串的特征,具有某种特点,字符段匹配
# 表达文本类型的特征(病毒,入侵等)
# 同时查找或替换一组字符串
# 匹配字符穿的全部或部分

# 正则表达式有字符和操作符组成的,转义
# .表示任何单个字符 [] [^]
# *出现0次或以上 +出现1次或以上 ?是否出现 |左右表达式任取其一
# {m} {m,n} 扩展前面一个字符 {0:3}扩展0次到3次
# ^abc表示abc在字符串开头,abc$表示abc在字符串结尾
# ()分组标记 \d等价[0-9] \w等价[A-Za-z0-9]
# 常见的正则表达式
# [\u4e00-\u9fa5]  匹配中文字符
# [1-9]\d{5}  中国境内邮政编码6位

# 原生字符串raw string
# string类型,需要考虑斜杠,转义字符
# 搜索与替换
# re库的主要函数 .search(pattern,string,flags=0)搜索匹配正则表达式的第一个位置,返回match对象
# flags re.I re.M re.S
# match()给定字符串 开始位置 起匹配,返回match()
# findall()搜索字符串,以列表类型返回全部能匹配的子串
#  split(pattern,string,maxsplit,flags)将一个字符串按照正则表达式匹配结果进行分割,返回列表类型
# maxsplit最大分割数,剩余部分作为最后一个元素输出
#  finditer()搜索字符串,返回一个匹配结果的迭代类型,每个迭代元素是match对象
#  sub(pattern,repl,string,count=0,flags=0)在一个字符串中替换所有匹配正则表达式的子串,返回替换后的字符串
# repl替换匹配字符串的字符串,count匹配的最大替换次数

# match=re.search(r'[1-9]\d{5}','BIT 100081')
# if match:
#     print(match.group(0))  # 输出匹配结果
# match=re.match(r'[1-9]\d{5}','BIT 100081')
# print(match.group(0))  #空变量,报错
# ls=re.findall(r'[1-9]\d{5}','BIT 100081 tsu100084')
# print(ls)  #输出列表对象
# ls=re.split(r'[1-9]\d{5}','BIT 100081 tsu100084')
# print(ls)
# ls2=re.split(r'[1-9]\d{5}','BIT 100081 tsu100084',maxsplit=1)
# print(ls2)
# str=re.sub(r'[1-9]\d{5}',':zipcode','BIT 100081 tsu100084')
# print(str)

# 函数调用式
# 面向对象用法:编译后的多次操作
# pat=re.compile(r'[1-9]\d{5}'),将正则表达式编译成正则表达式对象,再调用方法
# 然后调用方法,pat表示一组表达式 regex
# complie将正则表达式的字符串形式编译成正则表达式对象

# match对象
# 一次匹配结果,包含很多属性 string待匹配的文本,re使用的pattern,pos搜索文本的开始位置,endpos搜索文本的结束位置
# 方法group(0)获得匹配后的字符串,start()匹配字符串在原始字符串的开始位置,end()
# span()返回(.start(),.end())二元关系

# 存在多项匹配
# Re库默认采用贪婪匹配,即输出最长匹配字符串
# match=re.search(r'PY.*N','PYANBNCNDN')
# print(match.group(0))
# 修改一下,即可匹配最短字符串
# match=re.search(r'PY.*?N','PYANBNCNDN')
# print(match.group(0))
# 最小匹配操作付
# *?  前一个字符0次或无限次扩展,最小匹配
# +?  前一个字符1次或无限次扩展,最小匹配
# ??  前一个字符0次或1次扩展,最小匹配
# {m,n}?  扩展前一个字符m至n次(含n),最小匹配
