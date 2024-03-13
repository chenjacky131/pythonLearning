"""
os：Python内置的与操作系统文件相关的模块，该模块中语句的执行结果通常与操作系统有关，
即有些函数的运行效果在Windows操作系统和MacOS系统中不一样
函数名称                        描述说明
getcwd()                获取当前工作路径
listdir(path)           获取path路径下文件和目录信息，如果没有指定path，则获取当前路径下的文件和目录信息
mkdir(path)             在指定路径下创建目录
makedirs(path)          创建多级目录
rmdir(path)             删除path下的空目录
removedirs(path)        删除多级目录
chdir(path)             把path设置成当前目录
walk(path)              遍历目录树，结果为元组，包含所有路径名、所有目录列表和文件列表
remove(path)            删除path指定的文件
rename(old,new)         将old重命名为new
stat(path)              获取path指定的文件信息
startfile(path)         启动path指定的文件
"""
import os
import time

# print('当前工作路径：', os.getcwd())
# lst = os.listdir()
# print('当前路径下所有的目录和文件：', lst)
# print('指定路径下的所有的目录和文件：', os.listdir('D:/MyProject'))
# 创建目录
# os.mkdir('test')  # 如果要创建的文件夹存在，报FileExistsError错误
# os.makedirs('./aa/bb/cc')
# 删除目录
# os.rmdir('test')  # 如果要删除的目录不存在，报FileNotFoundError错误
# os.removedirs('aa/bb/cc')  # 如果要删除的目录不存在，报FileNotFoundError错误
# 改变当前工作路径
# os.chdir('D:/')
# print('当前工作路径：', os.getcwd())
# 遍历目录树,相当于递归
# for dirs, dirlst, filelst in os.walk('D:/MyProject/Local/pythonLearning'):
#     print(dirs)  # 父目录
#     print(dirlst)  # 子目录列表
#     print(filelst)  # 文件列表
#     print('-' * 10)

# 高级操作
# 删除文件
# os.remove('a.txt')  # 文件不存在时，报FileNotFoundError错误
# 重命名
# os.rename('aa.txt', 'aa_.txt')  # 文件不存在时，报FileNotFoundError错误


def date_format(time_stamp):  # 转换时间格式
    s = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time_stamp))
    return s


# 获取文件信息
info = os.stat('../aa_.txt')
print(info)
print('最近一次访问时间：', date_format(info.st_atime))
print('在windows操作系统中显示的文件的创建时间：', date_format(info.st_ctime))
print('最后一次修改时间:', date_format(info.st_mtime))
print('文件的大小（单位时字节）：', info.st_size)
# 启动路径下的文件
# os.startfile('calc.exe')
# 启动Python解释器
os.startfile("D:\SoftWare\Python3.11\python.exe")
