"""
将数据输出到文件中
注意点
1.所指的的盘符要存在
2.使用file=fp
"""

fp = open('./text.txt', 'a+')   # 如果文件不存在就创建，存在就文件内容的后面进行追加
print('Hello World', file=fp)
fp.close()

