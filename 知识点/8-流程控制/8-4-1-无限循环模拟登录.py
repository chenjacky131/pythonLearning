i = 0
while i < 3:
    user_name = input('请输入用户名：')
    password = input('请输入密码：')
    if user_name == 'tony' and password == '888':
        print('正在登录，请稍后。。。')
        i = 3
    else:
        if i < 2:
            print('用户名或者密码不正确，你还有', 2 - i, '次机会')
        i += 1
if i == 3:
    print('密码错误次数已达上限，限制登陆')