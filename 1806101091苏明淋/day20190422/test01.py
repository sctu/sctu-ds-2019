# 定义变量保存学生的姓名，年龄，性别
# -*- coding: utf-8 -*-
class Student:

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def study(self):
        print(self.name + 'studying!')

chen = Student('chen',18,'male')
chen.study()
