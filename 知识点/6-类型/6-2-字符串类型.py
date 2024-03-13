"""
字符串是python中的不可变数据类型
"""
str1 = 'str'
str2 = "str"
# 多行字符串单引号和双引号都可以
str3 = '''
我是第一行
我是第二行
'''
print(str1)
print(str2)
print(str3)
# 转义字符
print('hello\nworld')  # 换行符
print('helloo\tworld')  # 制表符，如果前面的已经占了一个，就占4-1个位置
print('hellooooo\tworld')  # 占4个字符
print('hello\rworld')  # 回车
print('hello\bworld')  # 退格
#  原字符 r或者R
print(r'hello\nworld')

# 字符串索引切片
s = 'HELLOWORLD'
print(s[0], s[-10])
print(s[0:1])  # 索引从0开始正向递增
print(s[-5:-4])  # 索引从-1开始逆向递减
print(s[:5])  # 默认N从0开始
print(s[0:])  # 默认M为字符串结束

# 字符串分解赋值
a, b, c, d, e = 'hello'
print(a, b, c, d, e)
# 模板字符串
name = 'tom'
print(f'他是{name}')
