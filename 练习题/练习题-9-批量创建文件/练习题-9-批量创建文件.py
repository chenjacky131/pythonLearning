import random


def gen_random_name(num):  # 批量生成文件名
    lst = ['水果', '烟酒', '粮油', '肉蛋', '蔬菜']
    hex_lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for i in range(1, num + 1):
        s = '{:04d}'.format(i)  # 名称的序号部分。显示4为长度的字符串，i不足4为用0补齐
        t = random.choice(lst)  # 名称的类别部分
        hex_p = ''
        for j in range(9):
            hex_p += random.choice(hex_lst)
        file_name = f'data/{s}_{t}_{hex_p}.txt'
        with open(file_name, 'w') as file:
            pass


if __name__ == '__main__':
    gen_random_name(10)
