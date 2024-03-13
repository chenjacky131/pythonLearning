"""
定义一个圆类-Circle，提供一个属性r（半径），提供两个方法：计算圆的面积get_area(self)和计算圆的周长get_perimeter(self)，
通过两个方法计算圆的周长和面积并且对计算结果进行输出，最后从键盘录入半径，创建圆类的对象，并调用计算面积和周长的方法输出面积和
周长。
"""
import math


class Circle:
    def __init__(self, r):
        self.r = int(r)

    def get_area(self):
        area = 3.14 * (self.r**2)
        print('圆的面积为：%.2f' % area)

    def get_perimeter(self):
        perimeter = 2 * 3.14 * self.r
        print('圆的周长为：%.2f' % perimeter)


radius = input('请输入圆的半径：')
cir = Circle(radius)
cir.get_area()
cir.get_perimeter()
