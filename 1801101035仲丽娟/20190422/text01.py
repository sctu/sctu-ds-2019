# -*- coding: UTF-8 -*-
#定义变量保存学生的姓名，年龄，性别

name = 'justin'
age = 18
gender = 'male'

a = 1
b = 2
c = 3


class Student:
#构造函数 __init__(self):
#类里面写的函数，第一个参数都是self
#__函数__都有特殊含义
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def study(self):
        print(self.name + ' studying!')
    def birth(self):
        print(self.name + ' 0101')


zhong = Student('zhong', 19, 'female')
zhong.study()
zhong.birth()
#print(zhong.name)
#print(zhong.age)
#print(zhong.gender)