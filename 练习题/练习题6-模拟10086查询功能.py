"""
模拟10086查询功能
"""
welcome_words = '''
-----------欢迎使用10086查询功能-----------
1.查询当前余额
2.查询当前剩余流量
3.查询当前剩余的通话时长
0.退出系统
'''
continue_searching = 'y'    # 循环判断条件
while continue_searching == 'y':
    print(welcome_words)
    option = input('请输入需要执行的操作:')
    match option:
        case '1':
            print('当前余额为：234.5元')
        case '2':
            print('当前剩余流量为4GB')
        case '3':
            print('当前剩余通话时长为500分钟')
        case '0':
            continue_searching = 'n'
        case _:
            print('输入有误，请重新输入')
            continue    # 退出本次循环，并且跳过下面循环部分的代码
    if continue_searching == 'y':
        continue_searching = input('还继续操作吗？y/n：')   # 循环判断条件重新赋值
else:
    print('欢迎再次使用10086查询功能!')
