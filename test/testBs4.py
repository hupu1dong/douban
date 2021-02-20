from bs4 import BeautifulSoup

file = open("./baidu.html","rb")
html = file.read().decode("utf-8")
bs = BeautifulSoup(html,"html.parser")

# print(bs.title)
# # print(bs.a)
# # print(type(bs.head))
# #1.Tag 标签及其内容；拿到他所找到的第一个内容
#
# print(bs.title.string)
# print(type(bs.title.string))
#
# #2.NavigableString  标签里的内容（字符串）
# print(bs.a.attrs)

# print(type(bs))     #表示整个文档
#
# print(bs.name)
# print(bs.attrs)
# print(bs)

# print(type(bs.a.string))

#--------------------------------------





#文档的遍历
# print(bs.head.contents[1])





#文档的搜索
#1 find_all()
#字符串过滤：会查找与字符串完全匹配的内容

# t_list = bs.find_all("a")
# print(t_list)

#正则表达式搜索：使用search()方法来匹配内容
import re
# t_list = bs.find_all(re.compile("a"))

# print(t_list)
#方法：传入一个函数（方法），根据函数的要求来搜索
# def name_is_exists(tag):
#     return tag.has_attr("name")
# n_list = bs.find_all(name_is_exists)
#
# for item in n_list:
#     print(item)
# print(n_list)

#kwargs 参数

# t_list = bs.find_all(id="u1")
# t_list = bs.find_all(class_="login-info")
# for item in t_list:
#     print(item)


#3.text参数

# t_list = bs.find_all(text="hao123")
# t_list = bs.find_all(text=["hao123","地图","贴吧"])
#t_list = bs.find_all(text = re.compile("\d"))
 #正则表达式来查询包含特定文本的内容

# t_list = bs.find_all("a",limit=5)
# for item in t_list:
#      print(item)

#4.选择器
# t_list = bs.select('title')
# t_list = bs.select('.mnav',limit=4)
# t_list = bs.select('#u1',limit=3)
# t_list = bs.select("a[class='c-color-gray2']")  #属性来查找
# t_list = bs.select("head > meta")  #通过子标签来查找

t_list = bs.select("")
for item in t_list:
    print(item)
