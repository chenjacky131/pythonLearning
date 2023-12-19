"""
使用列表存储一些商品数据，使用循环遍历输出商品信息，要求对商品的编号
进行格式化为6位，单价保留2位小数，并在前面添加人名币符号输出
"""
lst = [
    ['编号', '名称', '\t品牌', '单价'],
    ['01', '电风扇', '美的', 500],
    ['02', '洗衣机', 'TCL', 1000],
    ['03', '微波炉', '康佳', 400],
]
for index in range(len(lst)):
    for sub_index in range(len(lst[index])):
        item = lst[index][sub_index]
        print(item, end='\t\t')
    print()
print('-' * 50)
for index in range(len(lst)):
    for sub_index in range(len(lst[index])):
        item = lst[index][sub_index]
        if sub_index == 3 and index > 0:
            item = f'￥{item:.2f}'
        elif sub_index == 0 and index > 0:
            item = '0000' + item
        elif index == 0 and sub_index == 1:
            item = '\t' + item
        print(item, end='\t\t')
    print()
