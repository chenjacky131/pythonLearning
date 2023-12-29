"""
在一个函数的函数体内调用该函数本身，该函数就是递归函数
一个完整的递归操作由两部分组成，一部分时递归调用，一部
分是递归终止条件，一般可使用if-else结构来判断递归的
调用和递归的终止。
"""


def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)


print(fac(4))


def fac2(n):  # 1,1,2,3,5斐波那契数列
    if n == 1 or n == 2:
        return 1
    else:
        return fac2(n - 1) + fac2(n - 2)


print(fac2(5))
