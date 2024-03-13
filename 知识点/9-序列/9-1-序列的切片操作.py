s = 'hello-world'
s1 = s[0:5:2]   # [start:end:step]不包含end。start可以省略，默认为0。end可省略，默认为序列长度。step可省略，默认为1。
print(s1)
print(s[0::])
#   步长为负数
print(s[::-1])
print(s[-1:-12:-1])     # 这行代码和上一行效果一样
