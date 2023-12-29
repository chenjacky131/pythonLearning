"""
使用input()获取一个字符串，编写并传参，使用isdigit()方法提取字符串中所有
的数字，并对提取的数字进行求和计算，最后将存储数字的列表和累加和返回
"""


def get_sum(_str):
    lst = []
    for item in _str:
        if item.isdigit():
            lst.append(int(item))
    print(f'提取的列表为：{lst}')
    return sum(lst)


result = get_sum(input('请输入一个字符串：'))
print(f'累加和为：{result}')
