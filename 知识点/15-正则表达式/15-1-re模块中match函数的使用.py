"""
re模块  Python中的内置模块，用于实现正则表达式操作
re.match(pattern, string, flags=0)  用于从字符串的开始位置进行匹配，如果起始位置匹配成功，结果为match对象，否则为None
re.search(pattern, string, flags=0)  用于在整个字符串中搜索第一个匹配的值，如果匹配成功，结果为match对象，否则结果为None
re.findall(pattern, string, flags=0)  用于在整个字符串所有所有符合正则表达式的值，结果是一个列表类型
re.sub(pattern, repl, string, count, flags=0)  用于实现对字符串中指定字串的替换
re.split(pattern, string, maxsplit, flags=0)  字符串中的split方法功能相同，只是分隔字符串
"""
import re
pattern = '\d\.\d+'
s = '3.11 I study Python everyday'
match = re.match(pattern, s, re.I)
print(match)
print('匹配值的起始位置', match.start())
print('匹配值的结束位置', match.end())
print('匹配区间的位置元素', match.span())
print('待匹配的字符串', match.string)
print('匹配的数据', match.group())
s = 'I study Python 3.11 everyday'
match2 = re.search(pattern, s, re.I)
print(match2)
print('匹配值的起始位置', match2.start())
print('匹配值的结束位置', match2.end())
print('匹配区间的位置元素', match2.span())
print('待匹配的字符串', match2.string)
print('匹配的数据', match2.group())
s = 'I study Python2.7 and Python3.11 everyday'
match3 = re.findall(pattern, s)
print(match3)
pattern = '黑客|破解|爬虫'
s = '我想学习python，想破解一些VIP视频，python可以实现爬虫吗？'
new_s = re.sub(pattern, '**', s)
print(new_s)
s = 'https://www.bilibili.com/video/BV1wD4y1o7AS/?p=74&spm_id_from=pageDriver'
pattern = '[?|&]'
lst = re.split(pattern, s)
print(lst)
