"""
bool(obj)  获取指定对象的布尔值
str(obj)  将指定对象obj转成字符串类型
int(x)  将x转成int类型
float(x)  将x转成float类型
list(sequence)  将序列转成列表类型
tuple(sequence)  将序列转成元组类型
set(sequence)  将序列转成集合类型
常用的数学函数
abs(x)  获取x的绝对值
divmod(x, y)  获取x与y的商和余数
max(sequence)  获取sequence的最大值
min(sequence)  获取sequence的最小值
sum(iter)  对可迭代对象进行求和运算
pow(x, y)  获取x的y次幂
round(x, d)  对x进行保留d位小数，结果四舍五入
常用的迭代器操作函数
sorted(iter)  对可迭代对象进行排序
reversed(sequence)  反转序列生成新的迭代器对象
zip(iter1, iter2)  将iter1与iter2打包成元组并返回一个可迭代的zip对象
enumerate(iter)  根据iter对象创建一个enumerate对象
all(iter)  判断可迭代对象iter中所有元素的布尔值是否都为True
any(iter)  判断可迭代对象iter中所有元素的布尔值是否都位False
next(iter)  获取迭代器的下一个元素
filter(function, iter)  通过指定条件过滤序列并返回一个迭代器对象
map(function, iter)  通过函数function对可迭代对象iter的操作返回一个迭代器对象
常用的其它内置函数
format(value, format_spec)  将value以format_spec格式进行显示
len(s)  获取s的长度或s元素的个数
id(obj)  获取对象的内存地址
type(x)  获取x的数据类型
eval(s)  执行s这个字符串所表示的python代码
"""
print('非空字符串的布尔值：', bool('hello'))
print('空字符串的布尔值：', bool(''))
print('空列表的布尔值：', bool([]))
print('空列表的布尔值：', bool(list()))
print('空元组的布尔值：', bool(()))
print('空元组的布尔值：', bool(tuple()))
print('空集合的布尔值：', bool(set()))
print('空字典的布尔值：', bool({}))
print('空字典的布尔值：', bool(dict()))
print('整数0的布尔值：', bool(0))
print(type(str([10, 20, 30])))
# print(int('98.7'))  # ValueError: invalid literal for int() with base 10: '98.7'
print(float('98.7'))
s = 'hello'
print(list(s))
print(tuple(s))
print(set(s))
print(divmod(10, 3))
print(sum([1, 2, 3]))
print(round(4.126, 2))
print(round(314.15, -1))
lst = [54, 56, 77, 4, 567, 34]
asc_lst = sorted(lst)
desc_lst = sorted(lst, reverse=True)
reversed_lst = reversed(lst)
print('原列表：', lst)
print('升序列表：', asc_lst)
print('降序列表：', desc_lst)
print(reversed_lst)  # <list_reverseiterator object at 0x000001302328BF40>
print('反向列表：', list(reversed_lst))
x = ['a', 'b', 'c', 'd', 'e']
y = [10, 20, 30, 40, 50]
zip_obj = zip(x, y)
print(zip_obj)  # <zip object at 0x0000017779D67A40>
print(list(zip_obj))
print(any(['False']))
print(format(3.14, '20'))  # 数值类型默认右对齐
print(format('hello', '20'))    # 字符串类型默认左对齐
print(format('hello', '*<20'))  # <左对齐，*表示填充符，20表示的是显示的宽度
print(format('hello', '*>20'))  # 右对齐
print(format('hello', '*^20'))  # 居中对齐
