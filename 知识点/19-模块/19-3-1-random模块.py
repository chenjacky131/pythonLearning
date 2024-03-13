"""
函数名称                            功能描述
seed(x)                 初始化给定的随机数种子，默认位当前系统时间，确保代码每次运行都回得到相同结果。
random()                产生一个[0.0, 1.0)之间的随机数
randint(a,b)            生成一个[a,b]之间的证书
randrange(m, n, k)      生成一个[m, n)之间步长为k的随机整数
uniform(a, b)           生成一个[a,b]之间的随机小数
choice(seq)             从序列中随机选择一个元素
shuffle(seq)            将序列seq中元素随机排列，返回打乱后的序列
"""
import random
random.seed(10)
print(random.random())
