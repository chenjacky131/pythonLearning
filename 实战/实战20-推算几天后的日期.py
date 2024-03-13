"""
编写一个程序，输入开始日期和间隔天数，可以推算出结束日期，
使用内置的datetime模块
"""
from datetime import datetime, timedelta


def input_date():  # 输入日期函数
    _date = input('请输入开始日期：(20240101)后按回车：')
    date_str = f'{_date[0:4]}-{_date[4:6]}-{_date[6:8]}'  # 切片切出年月日
    dt = datetime.strptime(date_str, '%Y-%m-%d')  # 类型转换
    return dt


if __name__ == '__main__':  # 主程序运行
    start_date = input_date()
    # 输入间隔天数
    int_day = eval(input('请输入间隔天数：'))
    end_date = start_date + timedelta(days=int_day)
    print(f'您推送的日期是：{end_date}')
