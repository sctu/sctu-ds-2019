 # -*- coding: UTF-8 -*-

# 定义变量保存学生的姓名、年龄、性别
name = 'justin'
age = 18
gender = 'male'

a = 1
b = 2
c = 3


class Student:

    # 构造函数      gendar：性别
    # 类里面写的函数，第一个参数都是self
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # def study(self):
    #     print(self.name + ' studying!')

    def sing(self):
        print(self.name + ' is a singer')

# roy= Student('roy', 18, 'male')
# roy.study()

roy= Student('roy', 18, 'male')
roy.sing()
# roy=student('roy',18,'male')
# print(roy.name)
# print(roy.age)
# print(roy.gender)


