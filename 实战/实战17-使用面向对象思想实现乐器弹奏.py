"""
乐手可以弹奏不同的乐器从而发出不同的声音。可以弹奏的乐器包括二胡、钢琴
和琵琶。定义乐器类Instrument，包括方法make_sound()定义乐器类的子类：
二胡Erhu、钢琴Piano和小提琴Violin，定义一个函数可以弹奏各种乐器play(instrument),
测试给乐手不同的乐器让他弹奏。
"""
class Instrument:
    def make_sound(self):
        pass


class Erhu(Instrument):
    def make_sound(self):
        super().make_sound()
        print('二胡在演奏')


class Piano(Instrument):
    def make_sound(self):
        super().make_sound()
        print('钢琴在演奏')


class Violin(Instrument):
    def make_sound(self):
        super().make_sound()
        print('小提琴在演奏')


def play(instrument):
    instrument.make_sound()


erhu = Erhu()
piano = Piano()
violin = Violin()
play(erhu)
play(piano)
play(violin)
