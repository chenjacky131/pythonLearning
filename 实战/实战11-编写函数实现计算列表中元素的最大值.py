"""
随机产生10个元素，存储到列表中，编写函数获取这个列表中元素的最大值
（不能使用内置函数max）
"""
import random
lst = []
for i in range(10):
    lst.append(random.randint(1, 100))
print(lst)


def get_max_num(_lst):

    max_num = 0
    for num in _lst:
        if num > max_num:
            max_num = num
    return max_num


print(get_max_num(lst))
