"""
交集(公共部分) A&B
并集(合起来的所有) A|B
差集(A和B不一样的部分) A-B
补集(剔除公共部分后的所有) A^B
"""
A = {10, 20, 30, 40, 50}
B = {30, 50, 80, 100}
print(A & B)  # {50, 30}
print(A | B)  # {100, 40, 10, 80, 50, 20, 30}
print(A - B)  # {40, 10, 20}
print(A ^ B)  # {100, 40, 10, 80, 20}
# 向集合中添加元素
s = {10, 20, 30}
s.add(100)
print(s)
# 删除元素
s.remove(100)
print(s)
# 清空集合中的所有元素
s.clear()
print(s)
# 集合的遍历
s = {10, 20, 30}
for item in s:
    print(item)
# 使用enumerate遍历集合
for index, item in enumerate(s):
    print(index, '-->', item)
# 集合的生成式
s = {i for i in range(1, 10)}
print(s)
s = {i for i in range(1, 10) if i % 2 == 0}
print(s)
