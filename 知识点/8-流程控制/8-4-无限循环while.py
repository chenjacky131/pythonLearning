answer = input('今天上课吗？y/n ')
while answer == 'y':
    print('好好学习，天天向上。')
    answer = input('今天上课吗？y/n ')
# while的扩展
s = 0
i = 1
while i <= 100:
    s += i
    i += 1
else:
    print('1-100直接的累加和是：', s)