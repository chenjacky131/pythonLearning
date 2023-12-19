"""
str.isdigit  所有的字符都是数字（十进制的阿拉伯数字）
str.isnumeric  所有的字符都是数字
str.isalpha  所有的字符都是字符（包含中文字符）
str.isalnum 所有的字符都是数字或字母（包含中文字符）
str.islower  所有字符都是小写
str.isupper  所有字符都是大写
str.istitle  所有字符都是首字母大写
str.isspace  所有字符都是空白字符（\n、\t等）
"""
print('1232'.isdigit())  # True
print('111'.isnumeric())  # True
print('一二三'.isnumeric())  # True
print('Ⅲ'.isnumeric())  # True
print('壹'.isnumeric())  # True
print('hello你好'.isalpha())  # True
print('hello你好一二三'.isalpha())  # True
print('hello你好Ⅰ'.isalnum())  # True
print('hello你好123'.isalnum())  # True
print('helloworld'.islower())  # True
print('你好helloworld'.islower())  # True
print('HELLOWORLD你好'.isupper())  # True
print('Helloworld你好'.istitle())  # True
print('Hello World你好'.istitle())  # True
print('  '.isspace())  # True
print('\t'.isspace())  # True
print('\n'.isspace())  # True
