"""
1.结构模型匹配
    match data:
        case {}:
            pass
        case []:
            pass
        case _:
            pass
2.字典合并运算符|
3.同步迭代
    match data1,data2:
        case data1,data2:
            pass
"""
# data = eval(input('请输入要匹配的数据：'))
# match data:
#     case {'name': 'tom', 'age': 18}:
#         print('字典')
#     case [10, 20, 30]:
#         print('列表')
#     case _:
#         print('其它类型')
# 字典的合并
d1 = {'a': 10, 'b': 20}
d2 = {'c': 30, 'd': 40}
print(d1 | d2)
# 同步迭代
fruits = ('apple', 'orange', 'pear', 'grape')
counts = [10, 3, 4, 5]
for f, c in zip(fruits, counts):
    match f, c:
        case 'apple', 10:
            print('10个苹果')
        case 'orange', 3:
            print('3个橙子')
        case 'pear', 4:
            print('4个梨')
        case 'grape', 5:
            print('5个葡萄')
