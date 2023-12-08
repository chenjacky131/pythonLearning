"""
lst = [1, 2, 3]
1.使用[]定的可变序列，元素与元素之间用英文逗号隔开，列表中的元素可以是任意类型的数据
2.可以直接使用[]创建，也可以用list内置函数创建
列表名 = [element1, element2, ...]
列表名 = list(序列)
3.列表的删除del,del lst
"""
lst = ['hello', 'world', 98, 100.3]
print(lst)
lst2 = list('helloWorld')
print(lst2)
lst3 = list(range(0, 10, 2))
print(lst3)
# 列表是序列中的一种，对序列的操作符、运算符、函数均可以使用
print(lst + lst2 + lst3)
print(lst * 3)
