"""
被称为requests库，是用于处理HTTP（Hypertext Transfer Protocol超文本传输协议）
请求的第三方库，该库在爬虫程序中应用非常广泛。
使用requests库中的get()函数可以打开一个网络请求，并获取一个Response响应对象。响应
结果中的字符串数据可以通过响应对象的text属性获取，响应结果中除了有字符串数据也有二进制数据，
响应结果中的二进制数据可以通过响应对象的content属性获取。
"""
import requests
import re
url = 'http://www.weather.com.cn/weather1d/101230201.shtml'
resp = requests.get(url)
# 设置一下编码模式
resp.encoding = 'utf-8'
# print(resp.text)
city = re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>', resp.text)
weather = re.findall('<span class="weather">([\u4e00-\u9fa5]*)</span>', resp.text)
wd = re.findall('<span class="wd">(.*)</span>', resp.text)
zs = re.findall('<span class="zs">([\u4e00-\u9fa5]*)</span>', resp.text)
# print(city)
# print(weather)
# print(wd)
# print(zs)
lst = []
for a, b, c, d in zip(city, weather, wd, zs):
    lst.append([a, b, c, d])
print(lst)
for item in lst:
    print(item)

# 抓取百度logo
url2 = 'https://www.baidu.com/img/PCfb_5bf082d29588c07f842ccde3f97243ea.png'
resp = requests.get(url2)
# 保存到本地
with open('logo.png', 'wb') as file:
    file.write(resp.content)
