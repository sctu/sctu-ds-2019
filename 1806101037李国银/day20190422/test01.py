# -*- coding: UTF-8 -*-
# 定义变量保存学生的姓名，年龄，性别

name = '李国银'
age = '19'
gender = 'male'


class  Student:

    # init 是构造函数
    # 在类里面写的函数，第一个参数都是self
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def study(self):
        print(self.name + 'studying!')

    def ability(self):
        print(self.name + 'flying!')

    def hobby(self):
        print(self.name + 'do well in Cross Fire!')


li = Student('李国银','19','male')
li.study()
li.ability()
li.hobby()

# print(chen.name)
# print(chen.age)
# print(chen.gender)
