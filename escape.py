# 转义字符
print('hello\nworld')
print('helloo\tworld')  # 如果前面的已经占了一个，就占4-1个位置
print('hellooooo\tworld')  # 占4个字符
print('hello\rworld')  # 回车
print('hello\bworld')  # 退格
#  原字符 r或者R
print(r'hello\nworld')