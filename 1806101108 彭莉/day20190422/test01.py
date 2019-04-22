# -*- coding: UTF-8 -*-
# 定义变量保存学生的姓名,年龄,性别
name = 'justin'
age = 18
gender = 'male'

name2 = 'bob'
age2 = 19
gender2 = 'male'


class Student:
    # 构造函数
    # 类里面写得函数，第一个参数都是self
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def study(self):
        print(self.name + 'studying!')

chen = Student('chen', 18, 'male')
chen.study()
# print(chen.name)
# print(chen.age)
# print(chen.gender)

peng = Student('peng', 18, 'female')
peng.study()
# print(peng.name)
# print(peng.age)
# print(peng.gender)