"""
存储在计算机的存储设备中的一组数据序列就是文件
不同类型的文件通过后缀名进行区分
文本文件：由于编码格式的不同，所占磁盘的空间字节数不同
二进制文件：没有统一的编码，文件直接由0或1组成，需要使用指定的软件才能打开
Python操作文件的步骤：
    1打开文件
        变量名=open(filename, mode, encoding)
    2操作文件
        变量名.read()
        变量名.write(s)
    3关闭文件
        变量名.close()
"""


def my_write():
    # 1(创建)打开文件
    file = open('a.txt', 'w', encoding='utf-8')
    # 2操作文件
    file.write('伟大的中国梦')
    # 3关闭


def my_read():
    # 1(创建)打开文件
    file = open('a.txt', 'r', encoding='utf-8')
    # 2操作文件
    s = file.read()
    print(type(s), s)
    # 3关闭文件
    file.close()


# 主程序运行
if __name__ == '__main__':
    # my_write()
    my_read()