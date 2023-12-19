"""
声明一个字符串，内容为"HelloPython, HelloJava， HelloPhp",
用户从键盘录入要查询的字符（不区分大小写），要求统计出要查找的字符
在字符串中出现的次数
"""
s = 'HelloPython, HelloJava， HelloPhp'
word = input('请输入要查询的字符串：')
count = s.lower().count(word.lower())
print('{0}在{1}中一共出现了{2}次'.format(word, s, count))
