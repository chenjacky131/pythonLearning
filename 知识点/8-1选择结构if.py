input_number = eval(input('请输入彩票号码：'))
if input_number == 888:
    print('一等奖!')
else:
    print('谢谢参与')
# 如果语句块只有一句代码，可以将语句写在冒号后面
a = 12
b = 11
if a > b:
    print('a>b')
# if,else赋值
result = '你未中奖' if False else '中大奖了'
print(result)
# 多分枝结构
score = eval(input('请输入你的成绩：'))
if 0 > score or score > 100:
    print('成绩无效')
elif 0 <= score < 60:
    print('E')
elif 60 <= score < 70:
    print('D')
elif 70 <= score < 80:
    print('C')
elif 80 <= score < 90:
    print('B')
else:
    print('A')
# 嵌套结构
answer = input('您喝酒了吗？')
if answer == 'y':
    proof = eval(input('输入酒精度：'))
    if proof > 125:
        print('酒驾')
    else:
        print('没事了')
# 多个条件的连接
username = input('请输入用户名：')
password = input('请输入密码：')
if username == 'tony' and password == '8888':
    print('登录成功！')
else:
    print('登录失败！')
