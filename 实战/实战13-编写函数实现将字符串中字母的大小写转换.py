"""
使用input()获取一个字符串，编写并传参，将字符串中所有的小写
字母转成大写字母，将大写字母转成小写字母
"""


def trans_case(_str):
    lst = []
    for item in _str:
        if item.isupper():
            item = item.lower()
        elif item.islower():
            item = item.upper()
        lst.append(item)
    return ''.join(lst)


result = input('请输入一个字符串：')
print(trans_case(result))
