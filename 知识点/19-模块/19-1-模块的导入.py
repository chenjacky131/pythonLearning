"""
模块编写完成就可以被其它模块进行调用并使用被调用模块中的功能
import导入方式的语法结构：
    import 模块名称
    import 模块名称 [as 别名]
    import 模块1,模块2,...
from 模块名称 import 变量/函数/类/*
    导入模块中具有同名的变量和函数，后导入的会将之前导入的进行覆盖
    如果不想覆盖，则用import导入，然后用模块名打点调用
"""
import my_info  # import ...
import my_info as info  # import ... [as 别名]
from my_info import name  # from ... import 变量/函数/类/*
from my_info import *  # 通配符
import math, random, time  # 同时导入多个模块
print(my_info.name)
my_info.say()
print('*'*10)
print(info.name)
info.say()
print(name, say)
print(math, random, time)

