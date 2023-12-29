"""
继承
    在python中一个子类可以继承N多个父类
    一个父类也可以拥有N多个子类
    如果一个类没有继承任何类，那么这个类默认继承的是object类
继承的语法结构
    class 类名(父类1,父类2,...,父类N):
        pass
"""


class Person:   # 默认继承了object
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'大家好，我叫{self.name}，我今年{self.age}岁')


# Student继承Person类
class Student(Person):
    def __init__(self, name, age, num):
        super().__init__(name, age)  # 调用父类的初始化方法
        self.num = num


# Doctor继承Person类
class Doctor(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department


# 创建第一个子类对象
stu = Student('托尼', 12, 8888)
stu.show()
print(stu.num)
