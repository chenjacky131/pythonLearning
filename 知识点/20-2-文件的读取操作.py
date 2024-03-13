def my_read(filename):
    # 打开
    file = open(filename, 'w+', encoding='utf-8')
    # 操作
    file.write('你好啊\n')  # 写入完成
    file.write('好是很好')  # 写入完成
    # seek修改文件指针的位置
    file.seek(0)
    # 读取
    # s = file.read()  # 读取全部
    # s = file.read(2)  # 读取两个字符(你好)
    # s = file.readline()  # 读取一行数据
    # s = file.readline(2)  # 读取一行中的两个字符
    # s = file.readlines()  # 读取所有,一行为列表中的一个元素
    file.seek(3)  # 3个字节,一个中文占3个字节,utf-8
    s = file.read()
    print(type(s), s)
    # 关闭
    file.close()


if __name__ == '__main__':
    my_read('c.txt')
