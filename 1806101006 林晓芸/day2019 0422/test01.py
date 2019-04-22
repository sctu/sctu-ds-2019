# -*- coding: UTF-8 -*-

# 定义变量保存学生的，年龄，性别
name = "justin"
age = 18
gender = "male"

a = 1
b = 2
c = 3


class Student:

    # 构造函数
    # 类里面写的函数，第一个参数都是self
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def study(self):
        print(self.name + ' stuaying!')

    def sleep(self):
        print(self.name + ' sleeping!')

    def eat(self):
        print(self.name + ' eating!')


chen = Student('chen', 18, 'male')
chen.study()
chen.sleep()
chen.eat()

# print(chen.name)
# print(chen.age)
# print(chen.gender)
#
# bob = Student('bob', 19, 'female')
# print(bob.name)
# print(bob.age)
# print(bob.gender)





