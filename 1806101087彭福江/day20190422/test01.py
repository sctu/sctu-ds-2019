#定义变量保存学生的姓名、年龄、性别
# -*- coding: utf-8 -*-

name = "justin"
age = 18
gender = "male"


class Student:
    #构造函数
    #类里面写的函数，第一参数都是self
    def __int__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender =gender

   # def study(self):
        print(self.name+"studying")

chen = Student("chen",18,"male")
print(chen.name)
print(chen.age)
print(chen.gender)
