"""
列表生成式的语法结构
lst = [expression for item in range]
lst = [expression for item in range condition]
"""
import random
lst = [item for item in range(1, 11)]
print(lst)
lst = [item*item for item in range(1, 11)]
print(lst)
lst = [random.randint(1, 100) for _ in range(100)]
print(lst)
# 从列表中选择符合条件的元素组成新的列表
lst = [i for i in range(10) if i % 2 == 0]
print(lst)
# 创建二维列表
lst = [
    ['城市', '环比', '同比'],
    ['北京', '100', '83'],
    ['深圳', '89', '88'],
    ['广州', '78', '77']
]
print(lst)
# 遍历列表用双层for循环
for row in lst:  # 行
    for item in row:  # 列
        print(item, end='\t')
    print()
# 列表生成式生成一个4行5列的二维列表
lst = [[j for j in range(5)] for i in range(4)]
print(lst)
