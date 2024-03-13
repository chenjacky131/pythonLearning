def copy(src, new_path):
    # 文件的复制就是边读边写操作
    # 打开源文件
    file1 = open(src, 'rb')
    # 打开目标文件
    file2 = open(new_path, 'wb')
    # 开始复制,边读边写
    s = file1.read()  # 源文件读取
    file2.write(s)  # 目标文件写入
    # 关闭
    file2.close()
    file1.close()  # 先打开的后关,后打开的先关


if __name__ == '__main__':
    source_src = 'pic.jpg'
    target_path = 'pic_copy.jpg'
    copy(source_src, target_path)
    print('文件复制完毕!')
