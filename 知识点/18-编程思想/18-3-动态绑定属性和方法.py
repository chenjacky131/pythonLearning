

class Student:
    # 类属性：定义在类中，方法外的变量
    school = '北京大学'

    # 初始化方法
    def __init__(self, name, age):  # name是方法的参数，是局部变量，作用域是整个init方法
        self.name = name  # 左侧是实例属性，name是局部变量。将局部变量name的值赋值给实例属性name。实例属性的名称可以和局部变量相同。
        self.age = age

    # 定义在类中的函数，称为方法，自带一个self参数
    def show(self):
        print(f'我叫：{self.name}，今年{self.age}岁。')


stu = Student('诺格', 12)
# 为stu动态绑定一个实例属性
stu.gender = '男'
print(stu.gender)
# 动态绑定方法


def introduce():
    print('我是一个普通的函数，我被动态绑定成了stu对象的方法')


stu.fun = introduce  # 函数的赋值
stu.fun()
