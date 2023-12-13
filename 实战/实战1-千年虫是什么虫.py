"""
已知一个列表中存储的是员工的出生年份[88, 89, 90, 98, 00, 99]，
由于时间比较久，出生的年份均为2位的整数，现需要2位年份前家19，
如果年份是00，将需要加上200.
"""
lit = [88, 89, 90, 0, 99]
lit_new = []
print('原列表：', lit)
# 方式1，for in循环列表

# for item in lit:
#     if item == 0:
#         lit_new.append('200' + str(item))
#     else:
#         lit_new.append('19' + str(item))

# 方式2，len，range循环index

# for index in range(len(lit)):
#     if lit[index] == 0:
#         lit_new.append('200' + str(lit[index]))
#     else:
#         lit_new.append('19' + str(lit[index]))

# 方式3， enumerate遍历列表

for _, item in enumerate(lit):
    if item == 0:
        lit_new.append('200' + str(item))
    else:
        lit_new.append('19' + str(item))
print(lit_new)
