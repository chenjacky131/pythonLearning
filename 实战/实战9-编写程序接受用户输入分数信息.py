"""
如果分数在0-100之间，输出成绩。如果成绩不在该范围内，抛出异常信息，
提示分数必须在0-100之间。
"""
try:
    score = int(input('请输入分数：'))
    if score < 0 or score > 100:
        raise Exception('分数不正确')
except Exception as e:
    print(e)
else:
    print(f'分数为：{score}')
