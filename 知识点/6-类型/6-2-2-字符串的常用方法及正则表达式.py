"""
str.lower()  将str字符串全部转成小写字母，结果为一个新的字符串
str.upper()  将str字符串全部转成大写字符，结果为一个新的字符串
str.split(sep=None)  把str按照指定的分隔符sep进行分隔，结果为列表类型
str.count(sub)  结果为sub这个字符串在str中出现的次数
str.find(sub)  查询sub这个字符串在str中是否存在，如果不存在结果为-1，如果存在，
    结果为sub首次出现的索引
str.index(sub)  功能和find相同，区别在于要查询的子字符串sub不存在时，程序报错
str.startswith(s)  查询字符串str是否以子字符串s开头
str.endswith(s)  查询字符串str是否以子字符串s结尾
str.replace(old, new, count)  使用new代替str字符串中所有的old字符串，结果时一个新的字符串。
    count替换次数，默认全部替换
str.center(width, fillchar)  字符串str在指定的宽度范围内居中，可以使用fillchar进行填充
str.join(iter)  在iter中的每个元素的后面都增加一个新的字符串str
str.strip(chars)  从字符串中去掉左侧和右侧chars中列出的字符串,不区分chars里面字母的先后顺序
str.lstrip(chars)  从字符串中去掉左侧chars中列出的字符串
str.rstrip(chars)  从字符串中去掉右侧chars中列出的字符串
"""
s = 'helloWorld'
print(s.lower())
print(s.upper())
print(s.split('W'))
print(s.count('o'))
print(s.find('e'))
print(s.index('e'))
print(s.startswith('h'))
print(s.endswith('d'))
print(s.replace('o', '*', 1))
print(s.center(20, '*'))
print(s.join('123'))
s = '     hello    World     '
print(s.strip())
print(s.lstrip())
print(s.rstrip())
s = 'ld-helloWorld-dl'
print(s.strip('dl'))
print(s.lstrip('ld'))
print(s.rstrip('dl'))
