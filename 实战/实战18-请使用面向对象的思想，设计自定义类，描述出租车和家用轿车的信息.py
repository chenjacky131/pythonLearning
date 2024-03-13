"""
出租车类：
    属性包括：车型，车牌，所属出租公司；方法包括：启动，停止
家用轿车：
    属性包括：车型，车牌，车主姓名；方法包括：启动，停止
分析出租车和家用轿车的公共成员，提取出父类-汽车类
利用继承机制，实现出租车类和家用轿车类
最后，分别测试出租车类和家用轿车类对象的相关方法
"""


class Car:  # 父类
    def __init__(self, model, plate_number):
        self.model = model
        self.plate_number = plate_number

    def start(self):
        pass

    def stop(self):
        pass


class Taxi(Car):
    def __init__(self, model, plate_number, company):
        super().__init__(model, plate_number)
        self.company = company

    def start(self):
        print('乘客您好！')
        print(f'我是{self.company}出租车公司的，我的车牌是：{self.plate_number}，您要去哪里？')

    def stop(self):
        print('目的地到了，请您付款下车，欢饮下次乘坐')


class Sedan(Car):
    def __init__(self, model, plate_number, owner):
        super().__init__(model, plate_number)
        self.owner = owner

    def start(self):
        print(f'我是{self.owner}，我的汽车我做主')

    def stop(self):
        print('目的地到了，我们去玩吧')


taxi = Taxi('比亚迪', '闽D88888', '银河出租')
sedan = Sedan('大众', '闽D66666', 'Tony')
taxi.start()
taxi.stop()
print('*' * 60)
sedan.start()
sedan.stop()
