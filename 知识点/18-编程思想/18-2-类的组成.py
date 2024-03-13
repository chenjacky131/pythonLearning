"""
类
    类属性
        直接定义在类中，方法外的变量
    实例属性
        定义在__init__方法中，使用self打点的变量
    实例方法
        定义在类中的函数，而且自带参数self
    静态方法
        使用装饰器@stiticmethod修饰的方法
    类方法
        使用装饰器@classmethod修饰的方法
"""


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

    # 静态方法
    @staticmethod
    def sm():
        print('这是一个静态方法，不能调用实例属性，也不能调用实例方法')

    # 类方法
    @classmethod
    def cm(cls):  # cls是class的简写
        print('这是一个类方法，不能调用实例属性，也不能调用实例方法')


# 创建类的对象
stu = Student('托尼', 18)
# 实例属性，使用对象名进行打点调用
print(stu.name, stu.age)
# 类属性，直接用类名打点调用
print(Student.school)
# 实例方法，使用对象名进行打点调用
stu.show()
# 类方法，使用类名打点调用
Student.cm()
# 静态方法，使用 类名打点调用
Student.sm()
