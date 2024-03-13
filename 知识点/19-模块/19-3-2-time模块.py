"""
函数名称                                功能描述
time()                      获取当前时间戳
localtime(sec)              获取指定时间戳对应的本地时间的struct_time对象
ctime()                     获取当前时间戳对应的易读字符串
strftime()                  格式化时间，结果为字符串
striptime()                 提取字符串的时间，结果为struct_time对象
sleep(sec)                  休眠sec妙

格式化字符串                  日期/时间                   取值范围
%Y                          年份                      0001~9999
%m                          月份                      01~12
%B                          月名                      January~December
%d                          日期                      01~31
%A                          星期                      Monday~Sunday
%H                          小时(24h制)                00~23
%I                          小时(12h制)                01~12
%M                          分钟                      00~59
%S                          秒                        00~59
"""
import time
now = time.time()
print(now)
obj = time.localtime()  # struct_time对象
print(obj)
obj2 = time.localtime(60)   # 60秒 1970年，1月1日，8时，1分，0秒
print(obj2)
print('年份：', obj2.tm_year)
print('月份：', obj2.tm_mon)
print('日期：', obj2.tm_mday)
print('时：', obj2.tm_hour)
print('分：', obj2.tm_min)
print('秒：', obj2.tm_sec)
print('星期：', obj2.tm_wday)  # [0,6] 3表示周四
print('今年的第多少天：', obj2.tm_yday)
print(time.ctime())  # 时间戳对应的易读字符串
# 日期时间格式化
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print(time.strftime('月份的名称：%B', time.localtime()))
print(time.strftime('星期的名称：%A', time.localtime()))
# 字符串转成struct_time对象
print(time.strptime('2024-01-18 14:59:00', '%Y-%m-%d %H:%M:%S'))
time.sleep(5)
print('我醒了')
