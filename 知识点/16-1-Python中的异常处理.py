"""
try...except的语法结构为：
    try:
        可能会抛出异常的代码
    except 异常类型:
        异常代码处理（报错后执行的代码）
try...except...except的语法结构为：
    try:
        可能会抛出异常的代码
    except 异常类型A:
        异常代码处理（报错后执行的代码）
    except 异常类型B:
        异常代码处理（报错后执行的代码）
try...except...except...else的语法结构为：
    try:
        可能会抛出异常的代码
    except 异常类型A:
        异常代码处理（报错后执行的代码）
    except 异常类型B:
        异常代码处理（报错后执行的代码）
    else:
        未抛出异常后将执行
try...except...except...else...finally的语法结构为：
    try:
        可能会抛出异常的代码
    except 异常类型A:
        异常代码处理（报错后执行的代码）
    except 异常类型B:
        异常代码处理（报错后执行的代码）
    else:
        未抛出异常后将执行
    finally:
        一定会执行

raise  抛出一个异常，从而提醒程序出现了异常情况，程序能够正确地处理这些异常的情况
    raise关键字的语法结构为：
        raise [Exception类型(描述信息)]

Python中常见的异常类型
ZeroDivisionError  当除数为0时，引发的异常
indexError  索引超出范围所引发的异常
KeyError  字典取值时key不存在的异常
NameError  使用一个没有声明的变量时引发的异常
SyntaxError  Python中的语法错误
ValueError  传入的值错误
AttributeError  属性或方法不存在的异常
TypeError  类型不合适引发的异常
IndentationError  不正确的缩进引发的异常
"""
# try:
#     num1 = int(input('请输入一个整数：'))
#     num2 = int(input('请输入另一个整数：'))
#     result = num1/num2
# except ZeroDivisionError:
#     print('除数为0')
# except ValueError:
#     print('输入了非整数')
# except BaseException:
#     print('未知异常')
# else:
#     print(result)
# finally:
#     print('结束')
try:
    gender = input('请输入性别：')
    if gender != '男' and gender != '女':
        raise Exception('性别只能是男或女')
except Exception as e:
    print(e)
