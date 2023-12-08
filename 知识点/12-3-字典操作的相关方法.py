"""
字典的方法
    d.keys()    获取所有的key数据
    d.values()  获取所有的value数据
    d.pop(key, default) key存在获取相应的值，同时删除key-value键值对，否则获取默认值
    d.popitem() 从字典尾部取出一个键值对，结果为元组类型，同时将key-value键值对从字典中删除
    d.clear()   清空字典中所有的键值对
"""
d = {'dog': 10, 'cat': 20, 'pig': 30}
print(d.keys())
print(d.values())
# print(d.pop('cat'))
# print(d.pop('chicken', 100))
# print(d.popitem())
# print(d.popitem())
# 向字典中添加元素
d['chicken'] = 100
print(d)
d.clear()
print(bool(d))  # 空字典的布尔值为False
