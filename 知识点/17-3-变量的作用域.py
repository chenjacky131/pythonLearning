"""
局部变量和全局变量同名时，局部变量的优先级更高
global定义全局变量
"""
a = 100


def calc(x, y):
    a = 50  # 局部变量和全局变量同名时，局部变量的优先级更高
    return x + y + a


result = calc(10, 20)
print(result)
print(a)


def calc2(x, y):
    global s
    s = 40  # 声明和赋值必须分开执行
    return s + x + y


result = calc2(10, 30)
print(result)
print(s)
