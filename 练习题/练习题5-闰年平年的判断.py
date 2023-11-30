"""
输入年份，判断是否是闰年。闰年的判断条件为：
能被4整除但是不能被100整除，或者能被400整除
"""
year = eval(input('请输入一个四位数年份：'))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year, '年是闰年')
else:
    print(year, '年是平年')
