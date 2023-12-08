"""
集合的创建方式有两种
1.直接使用{}创建集合
    s = {element1, element2, ......elementN}
2.使用内置set函数创建集合
    s = set(可迭代对象)
集合的删除
del s
"""
# 直接创建集合
s = {10, 20, 30}
print(s)
# 集合只能存储不可变数据类型
# s = {[10, 20], [20, 40]}
# print(s) TypeError: unhashable type: 'list'
# 使用set创建集合，空集合的布尔值是False
s = set()
print(s)
# 直接用{}创建的是字典
s = {}
print(s, type(s))
# 集合是无序的不重复的
s = set('helloWorld')
print(s)
s = set([10, 20, 30])
print(s)  # {10, 20, 30}
s = set(range(1, 10))
print(s)
# 集合属于序列的一种，序列的方法适用
print('max:', max(s))
print('min:', min(s))
print('len:', len(s))
print('9在集合中存在吗?', (9 in s))
print('9在集合中不存在吗?', (9 not in s))
