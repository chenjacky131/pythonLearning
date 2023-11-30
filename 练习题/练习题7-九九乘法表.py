"""
使用嵌套循环输出九九乘法表
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        result = j * i
        print(j, '*', i, '=', result, end='\t')     # 制表符控制空格
    print()
