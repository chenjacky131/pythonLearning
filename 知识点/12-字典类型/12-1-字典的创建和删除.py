# (1)创建字典
d = {10: 'dog', 20: 'cat', 30: 'chicken', 20: 'duck'}
print(d)    # key相同时，value值进行了覆盖
# (2)zip函数
lst1 = [10, 20, 30]
lst2 = ['dog', 'cat', 'chicken', 'duck']
zipObj = zip(lst1, lst2)
print(zipObj)    # <zip object at 0x0000019668A17140>
# print(list(zipObj))     # [(10, 'dog'), (20, 'cat'), (30, 'chicken')]
d = dict(zipObj)
print(d)
# (3)使用参数创建字典
d = dict(dot=10, cat=20, chicken=30)    # 等号左侧的时键，右侧的时值
print(d)
t = (10, 20, 30)
print({t: 'dog'})   # 元组作为key
# 字典属于序列
print('max:', max(d))
print('min:', min(d))
print('len:', len(d))
# 字典的删除
del d
# print(d)

