"""
可变参数又分为个数可变的位置参数和个数可变的关键字参数两种，其中个数可变的位置参数
是在参数前加一颗星（*para），para形式参数的名称，函数调用时可接收任意个
数的实际参数，并放到一个元组中。个数可变的关键字参数是在参数前加两颗星（**para），
在函数调用时可接收任意多个“参数=值”形式的参数，并放到一个字典中。
"""
# 个数可变的位置参数


def fun(*para):
    print(type(para))  # 元组类型
    for item in para:
        print(item)


# 调用
fun(10, 20, 30)
fun(10)
fun([10, 20, 30])
# 在调用时，参数前加一颗星，将列表进行解包
fun(*[10, 20, 30])
# 个数可变的关键字参数


def fun2(**para):
    print(type(para))  # 字典类型
    for key, value in para.items():
        print(key, '----', value)


# 调用
fun2(name='Tony', age=18, address='上海')
d = {'name': 'Tony', 'age': 18, 'address': '上海'}
fun2(**d)
