# 遍历字符串
for i in 'hello':
    print(i)
print('-'*30)
# range函数，产生一个n,m的整数序列。包含n，不包含m。
for i in range(1, 11):
    print(i)
# 扩展，for后面跟else
s = 0
for i in range(1, 11):
    s += i
else:
    print('1-10之间的累加和是：', s)
