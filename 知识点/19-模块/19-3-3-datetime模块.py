"""
类名                              功能描述
datetime.datetime               表示日期时间的类
datetime.timedelta              表示时间间隔的类
datetime.date                   表示日期的类
datetime.time                   表示时间的类
datetime.tzinfo                 时区相关的类
"""
from datetime import datetime
dt = datetime.now()
print(dt)
print(type(dt))
print('年：', dt.year, '月：', dt.month, '日：', dt.day, '时：', dt.hour, '分：', dt.minute, '秒：', dt.second)
# 比较两个datetime类型对象的大小
labor_day = datetime(2024, 5, 1, 0, 0, 0)
national_day = datetime(2024, 10, 1, 0, 0, 0)
print('2024年5月1日比2024年10月1日早吗？', labor_day < national_day)
# datetime类型与字符串进行转换
nowdt = datetime.now()
nowdt_str = nowdt.strftime('%Y/%m/%d %H:%M:%S')
print('nowdt的数据类型：', type(nowdt), 'nowdt所表示的数据是：', nowdt)
print('nowdt_str的数据类型是：', type(nowdt_str), 'nowdt_str所表示的数据是：', nowdt_str)
# 字符串类型转成datetime类型
str_datetime = '2024年1月18日15点44分'
dt3 = datetime.strptime(str_datetime, '%Y年%m月%d日%H点%M分')
print(dt3, type(dt3))
