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


def my_read():
    with open('student.csv', 'r') as file:
        s = file.read()
        lst = s.split(',')
        print(lst)


# 存储和读取二维数据
def my_write_table():
    lst = [
        ['商品名称', '单价', '采购数量'],
        ['水杯', '98.5', '20'],
        ['鼠标', '89', '100']
    ]
    with open('table.csv', 'w', encoding='utf-8') as file:
        for item in lst:  # item是列表类型
            data = ','.join(item)
            file.write(data)
            file.write('\n')


def my_read_table():
    data = []
    with open('table.csv', 'r', encoding='utf-8') as file:
        s = file.readlines()  # 每一行是列表中的一个元素
        for item in s:
            _str = item[:len(item) - 1]
            data.append(_str.split(','))
        print(data)


if __name__ == '__main__':
    # my_write()
    # my_read()
    # my_write_table()
    my_read_table()
