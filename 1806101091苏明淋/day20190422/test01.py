# -*- coding: utf-8 -*-
# 定义变量保存学生的姓名，年龄，性别


class Student:

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def study(self):
        print(self.name + 'studying!')
        print(self.age)
        print(self.gender)


chen = Student('chen', 18, 'male')
Tom = Student('Tom', 20, 'male')

chen.study()
Tom.study()
