t = ('python', 'php', 'node')
# 更具索引访问元组
print(t[2])
# 元组切片
t2 = t[0:3:2]
print(t2)
# 元组的遍历
for item in t:
    print(item)
# for range len索引遍历
for i in range(len(t)):
    print(i, t[i])
# 利用enumerate遍历
for index, item in enumerate(t):
    print(index, item)
