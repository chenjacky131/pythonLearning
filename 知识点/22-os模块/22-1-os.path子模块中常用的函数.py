"""
os.path模块：是os模块的子模块，也提供了一些目录或文件的操作函数
函数名称                            描述说明
abspath(path)               获取目录或文件的绝对路径
exists(path)                判断目录或文件在磁盘上是否存在，结果为bool类型，如果目录或文件在磁盘上存在，结果为True，否则为False
join(path, name)            将目录与目录名或文件名进行拼接，相当于字符串的”+“操作
splitext()                  分别获取文件名和后缀名
basename(path)              从path中提取文件名
dirname(path)               从path中提取路径（不包含文件名）
isdir(path)                 判断path是否是有效路径
isfile(path)                判断file是否是有效文件
"""
from os import path
print('获取目录或文件的绝对路径：', path.abspath('./aa_.txt'))
print('判断目录或文件在磁盘上是否存在：', path.exists('./aa_1.txt'))
print('拼接路径：', path.join('D:/MyProject', './aa_.txt'))
print('分隔文件名和文件后缀名：', path.splitext('./aa_.txt'))
print('提取文件名（包含后缀）：', path.basename('D:/SoftWare/Python3.11/python.exe'))
print('提取路径名：', path.dirname('D:/SoftWare/Python3.11/python.exe'))
print('判断有效路径：', path.isdir('D:/SoftWare/Python3.11'))
print('判断有效文件：', path.isfile('D:/SoftWare/Python3.11/python.exe'))
