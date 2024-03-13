"""
with语句：又称上下文管理器，在处理文件时，无论是否产生异常，
都能保证with语句执行完毕后关闭已经打开的文件，这个过程是自动
的，无需手动操作。
语法结构：with open(...) as file:
            pass
"""


def write_fun():
    with open('aa.txt', 'w', encoding='utf-8') as file:
        file.write('2022北京冬奥会欢迎你')


def read_fun():
    with open('aa.txt', 'r', encoding='utf-8') as file:
        print(file.read())


# 第三个函数
def copy(source_file, target_file):
    with open(source_file, 'r', encoding='utf-8') as file:
        with open(target_file, 'w', encoding='utf-8') as file2:
            file2.write(file.read())  # 将读取的内容直接写入文件


if __name__ == '__main__':
    write_fun()
    read_fun()
    # 文件复制
    copy('./aa.txt', '../aa_copy.txt')
