"""
返回值可以是一个值，或多个值，如果返回值是多个，结果是一个元组类型。
"""
# 返回值可以是多个


def get_sum(num):
    s = 0
    odd_sum = 0
    even_sum = 0
    for i in range(1, num + 1):
        s += i
        if i % 2 == 0:
            even_sum +=i
        else:
            odd_sum += i
    return s, odd_sum, even_sum


result = get_sum(10)
print(type(result))
print(result)
# 解包赋值
a, b, c = get_sum(10)
print(a, b, c)
