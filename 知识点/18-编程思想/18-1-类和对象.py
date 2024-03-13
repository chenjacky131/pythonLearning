"""
类是怎么来的
    是由N多个对象抽取出“像”的属性和行为从而归纳总结出来的一种类别
自定义数据类型的语法结构为
    class 类名():
        pass
创建对象的语法结构为
    对象名 = 类名(),括号可省略
"""


class Person:
    pass


per = Person()
print(type(per))
