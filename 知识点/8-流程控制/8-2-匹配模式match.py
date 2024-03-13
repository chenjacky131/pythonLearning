score = input('请输入成绩等级：')
match score:
    case 'A':
        print('优秀')
    case 'B':
        print('良好')
    case 'C':
        print('中等')
    case 'D':
        print('及格')
    case 'F':
        print('不及格')
    case _:  # 兜底的
        print('输入有误！')
