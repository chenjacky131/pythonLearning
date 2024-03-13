"""
所有类直接或者间接的父类
所有类都拥有object类的属性和方法
object类中特殊的方法：
    __new__ 由系统调用，用于创建对象
    __init__    创建对象时手动调用，用于初始化对象的属性值
    __str__     对象的描述，返回值是str类型，默认输出对象的内存地址
"""
class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f'我的名字叫：{self.name}')


per = Person('托尼')
print(dir(per))
print(per)
