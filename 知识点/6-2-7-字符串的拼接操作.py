"""
使用str.join进行拼接
直接拼接
使用格式化字符串进行拼接
"""
s1 = 'hello'
s2 = 'world'
# 使用+号进行拼接
print(s1 + s2)
# 使用join进行拼接
print(''.join([s1, s2]))
# 直接拼接
print('hello''world')
# 使用格式化字符串进行拼接
print('%s%s' % (s1, s2))
print(f'{s1}{s2}')
print('{0}{1}'.format(s1, s2))
