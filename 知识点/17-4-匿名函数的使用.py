"""
lambda  是指没有名字的函数，这种函数只能使用一次，一般是在函数的函数体
只有一句代码且只有一个返回值时，可以使用匿名函数来简化
语法结构 result=lambda 参数列表:表达式
"""
# 匿名函数
s = lambda a, b: a + b
# 调用匿名函数
print(s(10, 20))
# 对列表进行排序
student_score = [
    {'name': 'tom', 'score': 98},
    {'name': 'harry', 'score': 95},
    {'name': 'jack', 'score': 100},
    {'name': 'bruce', 'score': 65},
]
student_score.sort(key=lambda x: x.get('score'), reverse=True)
print(student_score)
