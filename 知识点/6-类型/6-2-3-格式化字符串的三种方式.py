"""
占位符
    %s  字符串格式
    %d  十进制整数格式
    $f  浮点数格式
f-string  Python3.6引入的格式化字符串的方式，以{}标明被替换的字符
str.format  模板字符串.format(逗号分隔的参数)
"""
name = '马冬梅'
age = 18
score = 87.8
print('姓名：%s 年龄：%d 分数：%f' % (name, age, score))  # 姓名：马冬梅 年龄：18 分数：87.800000
print('姓名：%s 年龄：%d 分数：%.1f' % (name, age, score))  # .1f保留一位小数
print(f'姓名：{name} 年龄：{age} 分数：{score:.3f}')
print('姓名：{0} 年龄：{1} 分数：{2}'.format(name, age, score))
print('姓名：{2} 年龄：{1} 分数：{0}'.format(score, age, name))
