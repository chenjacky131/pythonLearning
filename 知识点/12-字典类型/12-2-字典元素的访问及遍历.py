"""
字典元素的取值：
    d[key]或d.get(key)
字典元素的遍历：
    1：遍历出key和value的元组
        for element in d.items():
            pass
    2：分别遍历出key和value
        for key, value in d.items():
            pass
"""
d = {'cat': 10, 'dog': 20, 'chickens': 30}
# 访问字典中的元素
print(d['cat'])  # 如果key不存在，会报错
print(d.get('dog'))  # 可以指定默认值d.get('python', 30)
# 字典的遍历
for item in d.items():
    print(item)
for key, value in d.items():
    print(key, value)
