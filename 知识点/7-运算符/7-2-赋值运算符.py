"""
赋值运算符 =
x+=y x = x + y
x-=y x = x - y
x*=y x = x * y
x/=y x = x / y
x%=y x = x % y
x//=y x = x // y
x**=y x = x ** y
a=b=c=100   # 支持链式赋值，相当于x=100,b=100,c=100
a,b = 10,20 # 支持解包赋值，相当于a=10,b=20
"""
a, b = 10, 20
print(a, b)
a, b = b, a     # 交换变量的值
print(a, b)
