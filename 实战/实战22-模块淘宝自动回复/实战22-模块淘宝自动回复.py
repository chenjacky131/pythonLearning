"""
淘宝客服为了快速回复买家问题，设置了自动回复功能，当有买家咨询时，
客服自助系统会首先使用提前规划好的内容进行回复，请用Python程序
实现这一功能
"""


def find_answer(question):
    with open('./replay.txt', 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if line == '':
                break  # 退出while循环
            keyword = line.split('|')[0]  # 字符串的劈分操作
            reply = line.split('|')[1]
            if keyword in question:
                return reply
    return False


if __name__ == '__main__':
    q = input('HI,XXX,您好，有什么问题和我说说吧：')
    while True:
        if q == 'bye':
            break
        else:
            r = find_answer(q)  # 开始查找要回复的答案
            if not r:
                q = input('小蜜蜂不知道您在说什么，换个说法，退出请输入bye:')
            else:
                print(r)
                q = input('您还可以继续问我问题，退出请输入bye：')
    print('小主人再见')
