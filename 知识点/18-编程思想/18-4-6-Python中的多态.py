"""
多态
    指的就是多种形态，即便不知道一个变量所引用的对象到底是什么类型，仍然可以通过这个变量调用对象的方法。
    在程序运行过程中根据变量所引用对象的数据类型，动态决定调用哪个对象中的方法。
    Python语言中的多态，根本不关心对象的数据类型，也不关心类之间是否存在继承关系，只关心对象的行为（方法）。只要
        不同的类中有同名方法，即可实现多态。
"""


class Person:
    def eat(self):
        print('人吃五谷杂粮')


class Cat:
    def eat(self):
        print('猫吃鱼')


class Dog:
    def eat(self):
        print('狗吃肉')


#  这三个类中都有一个同名的方法， eat
def fun(obj):  # obj是函数的参数形式，在定义处知道这个参数的类型吗？
    obj.eat()


# 创建三个类的对象
per = Person()
cat = Cat()
dog = Dog()
# 调用fun函数
fun(per)
fun(cat)
fun(dog)
