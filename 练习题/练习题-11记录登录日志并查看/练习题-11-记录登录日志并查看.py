"""
创建XX客服管理系统的登录界面，每次登录时，将用户的登录日志写入文件中，
并且可以在程序中查看用户的登录日志
"""
import time


def login():  # 登录操作
    user_name = input('请输入用户名：')
    pass_word = input('请输入密码：')
    if user_name == pass_word:  # 简单的判断用户名和密码一样则登录成功
        with open(f'logs/log.txt', 'a') as file:  # 写入登录日志，a追加模式写入
            t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            file.write(f'用户名：{user_name},登录时间：{t}\n')
        print('登录成功')
        login_success_option()  # 登录成功后的操作
    else:
        print('用户名或密码不正确')
        login()


def login_success_option():  # 登录成功后的操作
    option_num = input('输入提示数字，执行相应操作：0.退出 1.查看登录日志\n输入操作数字：')
    if option_num == '0':
        print('退出成功')
        login()
    else:
        print('查看登录日志')
        get_log()
        login_success_option()


def get_log():  # 获取登录日志
    with open(f'logs/log.txt', 'r') as file:
        s = file.read()
        print(s)


if __name__ == '__main__':
    login()
