"""
执行输出区别表格
"""
title = ['数据类型 ', '序列类型 ', '元素是否可重复         ', '是否有序', '定义符号']
_list = ['列表list ', '可变序列 ', '可重复               ', '有序  ', '[]']
_tuple = ['元组tuple', '不可变序列', '可重复               ', '有序  ', '()']
_dict = ['字典dict ', '可变序列 ', 'Key不可重复，Value可重复', '无序  ', '{key:value}']
_set = ['集合set  ', '可变序列 ', '不可重复             ', '无序  ', '{}']
for i in range(0, 5):
    for j in range(0, 5):
        match i:
            case 0:
                print(title[j], end='\t\t')
            case 1:
                print(_list[j], end='\t\t')
            case 2:
                print(_tuple[j], end='\t\t')
            case 3:
                print(_dict[j], end='\t\t')
            case 4:
                print(_set[j], end='\t\t')
    print()
