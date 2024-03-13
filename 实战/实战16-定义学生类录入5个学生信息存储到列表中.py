"""
定义学生类Student，包含姓名，年龄，性别，分数四个属性，提供一个用于学生信息
输出的方法info(self)。编写测试代码，使用循环录入5位学生信息，由于录入的学
生信息中间使用“#”进行分隔，所以需要使用字符串的split()方法，进行劈分，使用
劈分的信息创建学生对象，使用列表存储学生信息，最后使用循环遍历列表，调用对象
的info()方法输出学员信息。
"""


class Student:
    def __init__(self, name, age, sex, score):
        self.name = name
        self.age = age
        self.sex = sex
        self.score = score

    def info(self):
        print(f'{self.name} {self.age} {self.sex} {self.score}')


n = 1
stu_list = []
while n < 5:
    stu_info = input(f'请输入第{n}位学生的姓名，年龄，性别，分数，中间用#号进行分隔：')
    info_arr = stu_info.split('#')
    stu = Student(info_arr[0], info_arr[1], info_arr[2], info_arr[3])
    stu_list.append(stu)
    n += 1
for s in stu_list:
    s.info()
