"""
数据的组织维度：也称为数据的组织方式或存储方式，在python中常用
的数据组织方式可分为一维数据、二维数据和高维数据。
一维数据：通常采用线性方式组织数据，一般使用Python中的列表、元组、或者集合进行存储数据。
二维数据：二维数据也称表格数据，由行和列组成，类似于Excel表格，在Python中使用二维列表进行存储。
高维数据：高维数据则是使用Key-Value方式进行组织数据，在Python中使用字典进行存储数据。
    在Python中内置的json模块专门用于处理JSON(Javascript Object Notation)格式的数据。
"""


def my_write():
    # 一维数据，可以使用列表、元组、集合
    lst = ['张三', '李四', '王五', '赵六', '苏七']
    with open('student.csv', 'w') as file:
        file.write(','.join(lst))  # 将列表转换成字符串


if __name__ == '__main__':
    my_write()
