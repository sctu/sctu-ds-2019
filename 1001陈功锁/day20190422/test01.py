# coding: utf-8

# 定义变量保存学生的姓名，年龄，性别
name = 'justin'
age = 18
gender = 'male'

a = 1
b = 2
c = 3


class Student:
    # 构造函数
    # 类里面写的函数，第一个参数都是self
    # __函数名__ 这类函数都有特殊含义
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 用户自定义函数
    def study(self):
        print(self.name + ' studying!')



chen = Student('chen', 18, 'male')
chen.name
chen.age
chen.gender
chen.study()

# 任务1：扩展学生属性，并进行测试。
# 任务2：扩展学生函数，并进行测试。

# print(chen.name)
# print(chen.age)
# print(chen.gender)
#
# bob = Student('bob', 19, 'female')
# print(bob.name)
# print(bob.age)
# print(bob.gender)



