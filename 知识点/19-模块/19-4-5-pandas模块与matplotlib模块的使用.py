"""
Pandas模块是基于numpy模块扩展的一个非常重要的数据分析模块，
使用pandas读取excel数据更加的方便。

Matplotlib是用于数据可视化的模块，使用Matplotlib.pyplot
可以非常方便的绘制饼图、柱形图、折线图。
"""
import pandas as pd
import matplotlib.pyplot as plt
# 读取Excel文件
df = pd.read_excel('测试数据.xlsx')
# print(df)
#  解决中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
#  设置画布的大小
plt.figure(figsize=(10, 6))
labels = df['景区']
y = df['气温']
# print(labels)
# print(y)
#   绘制饼图
plt.pie(y, labels=labels, autopct='%1.1f%%', startangle=90)
#  设置x,y轴刻度
plt.axis('equal')
plt.title('景区天气')
# 显示出来
plt.show()
