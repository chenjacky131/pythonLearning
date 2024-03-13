class Student:
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    # 使用@property修改方法，将方法转成属性使用
    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        if value != '男' and value != '女':
            print('性别有误，已将性别默认设置为男')
            self.__gender = '男'
        else:
            self.__gender = value


stu = Student('托尼', '男')
print(stu.gender)
stu.gender = '女'  # 未设置setter前报错：AttributeError: property 'gender' of 'Student' object has no setter
print(stu.gender)
stu.gender = 'gay'
print(stu.gender)
