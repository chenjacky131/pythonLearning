"""
变量的赋值
    只是形成两个变量，实际上还是指向同一个对象
浅拷贝
    拷贝时，对象包含的子类对象内容不拷贝，因此，源对象与拷贝对象会引用同一子对象
深拷贝
    使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也不相同
"""


class CPU:
    pass


class DISK:
    pass


class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


cpu = CPU()
disk = DISK()
com = Computer(cpu, disk)
#  变量对象的赋值
com1 = com
print(com)
print(com1)
#  类对象的浅拷贝
import copy
com2 = copy.copy(com)
print(com)
print(com2)
#  对象的深拷贝
com3 = copy.deepcopy(com)
print(com, '子对象的内存地址：', com.cpu, com.disk)
print(com3, '子对象的内存地址：', com3.cpu, com3.disk)
