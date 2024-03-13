"""
特殊属性                     功能描述
obj.__dict__    对象的属性字典
obj.__class__   对象所属的类
class.__bases__ 类的父类元组
class.__base__  类的父类
class.__mro__   类的层次结构
class.__subclasses__()  类的子类列表
"""


class A:
    pass


class B:
    pass


class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age


#  创建类的对象
a = A()
b = B()
c = C('托尼', 18)
print('对象c的属性字典：', c.__dict__)
print('对象所属的类：', c.__class__)
print('C类的父类元组：', C.__bases__)
print('C类的父类：', C.__base__)
print('C类的层级结构：', C.__mro__)
print('A类的子类列表：', A.__subclasses__())
