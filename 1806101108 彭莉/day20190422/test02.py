# -*- coding: UTF-8 -*-
# 定义变量保存学生的姓名,年龄,性别
name = 'justin'
age = 18
gender = 'male'

name2 = 'bob'
age2 = 19
gender2 = 'male'


class Student:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def sleep(self):
        print(self.name + ' is sleeping!')


Alice = Student('Alice', 18, 'female')
Alice.sleep()