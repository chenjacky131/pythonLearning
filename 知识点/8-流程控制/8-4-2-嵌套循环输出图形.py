# 三行四列
print('矩形')
for i in range(1, 4):
    for j in range(1, 5):
        print('*', end='')
    print()
print('-' * 30)
# 直角三角形
print('三角形')
for i in range(1, 6):
    for j in range(1, i + 1):
        print('*', end='')
    print()
print('-'*30)
# 等腰三角形
"""
&&&&*
&&&***
&&*****
&*******
*********
"""
print('等腰三角形')
for i in range(1, 6):
    for j in range(1, 6 - i):  # 画空格
        print(' ', end='')
    for j in range(1, i*2):  # 画*
        print('*', end='')
    print()

