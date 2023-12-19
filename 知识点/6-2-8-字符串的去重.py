s = 'helloworlddddddd'
# 字符串拼接
new_str = ''
for item in s:
    if item not in new_str:
        new_str += item
print(new_str)
# 使用集合去重+列表排序
new_str2 = set(s)
new_str2 = list(new_str2)
new_str2.sort(key=s.index)
new_str2 = ''.join(new_str2)
print(new_str2)

