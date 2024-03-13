from datetime import datetime
from datetime import timedelta
delta1 = datetime(2024, 10, 1, 0, 0, 0) - datetime(2024, 5, 1, 0, 0, 0)
print('delta1的数据类型是：', type(delta1), 'delta1所表示的数据是：', delta1)
print('2024年5月1日之后的153天是：', datetime(2024, 5, 1, 0, 0, 0) + delta1)
# 通过传入参数的方式创建一个timedelta对象
td1 = timedelta(10)
print('创建一个10天的timedelta对象', td1)
