import os


def gen_dir(num):  # 批量生成文件夹
    for i in range(1, num + 1):
        os.mkdir('./dirs/' + str(i))


if __name__ == '__main__':
    gen_dir(19)
