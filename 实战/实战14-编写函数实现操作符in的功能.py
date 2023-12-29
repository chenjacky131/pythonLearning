"""
使用input()从键盘获取一个字符串，判断这个字符串在列表中是否存在（函数体不能使用in），
返回结果True或False
"""


def fun_in(s, _lst):
    for item in _lst:
        if item == s:
            return True
    return False


lst = ['hello', 'world', 'python']
result = input('请输入要判断的字符串：')
print('存在' if fun_in(result, lst) else '不存在')
