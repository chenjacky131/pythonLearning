# break跳出循环
s = 0
i = 1
while i < 11:
    s += i
    if s > 20:
        print('累加和大于20的当前数是：', i)
        break
    i += 1
# continue退出当次循环，不执行continue后面的代码
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)
