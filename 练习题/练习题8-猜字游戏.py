"""
猜字游戏
randint(a,b)返回a-b之间的随机数，包含ab
"""
import random
random_number = random.randint(1, 100)  # 产生1-100之间的随机数
count = 1   # 记录猜字的次数
last_input = 0  # 上次输入的结果
min_num = 1  # 记录猜字区间的低位
max_num = 100  # 记录猜字区间的高位
while count <= 10:
    input_tips_word = '请输入' + str(min_num) + '-' + str(max_num) + '之间的数字:'
    number = eval(input(input_tips_word))
    last_input = number
    if number > random_number:
        max_num = number
        print('大了')
    elif number < random_number:
        min_num = number
        print('小了')
    else:
        print('恭喜你，猜对了!')
        break
    count += 1
else:
    print('很遗憾，你没有猜对')
