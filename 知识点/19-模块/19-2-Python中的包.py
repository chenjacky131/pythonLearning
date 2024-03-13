"""
含有__init__.py文件的文件夹（目录）
可以避免模块名称相冲突的问题
主程序运行(被其它模块导入不运行)
    if __name__ == '__main__':
        pass
"""
import admin.my_admin as a  # import 包名.模块名 [as 别名]
from admin import my_admin as b  # from 包名 import 模块名 [as 别名]
from admin.my_admin import info  # from 包名.模块名 import 变量/类/函数/*
a.info()
b.info()
info()

