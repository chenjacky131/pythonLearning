"""
使用列表存储N个车牌号码，通过遍历列表及字符串的切片操作判断车牌的归属地
"""
lst = ['京A8888', '闽D8888', '琼B9999', '粤A8888']
for item in lst:
    print(f'{item} 归属地 {item[0]}')
