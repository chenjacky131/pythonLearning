"""
方法重写
    子类继承了父类就拥有了父类中公有成员和受保护成员
    父类的方法并不能完全适合子类的需求，这个时候子类就可以重写父类的方法
    子类在重写父类方法时，要去方法的名称必须和父类的方法的名称相同，在子类重写后的方法中
        可以通过super().xxx()调用父类中的方法
"""


class FatherA:
    def __init__(self, name):
        self.name = name

    def showA(self):
        print('父类A中的方法')


class FatherB:
    def __init__(self, age):
        self.age = age

    def showB(self):
        print('父类B中的方法')


# 多继承
class Son(FatherA, FatherB):
    def __init__(self, name, age, gender):
        #  需要调用两个父类的初始化方法
        FatherA.__init__(self, name)
        FatherB.__init__(self, age)
        self.gender = gender

    def showB(self):
        super().showB()
        print(f'我是来自SON中的方法,我的性别是:{self.gender}')


son = Son('陈美美', 18, '女')
son.showA()
son.showB()
