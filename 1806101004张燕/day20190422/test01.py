# -*- coding: UTF-8 -*-
#定义变量保存所有学生的姓名、年龄、性别
name='jackson'
age=18
gender='male'


class Student:
    #构造函数
    #在类里面写的函数，的一个函数都是self
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def study(self):
        print(self.name+' is studying')

    def describe(self):
        print(self.name+' is a handsome boy')

    def hobby(self):
        print(self.name+' is good at dancing and singing')




jackson=student('jackson',18,'male')
jackson.study()
jackson.describe()
jackson.hobby()

# print(jackson.name)
# print(jackson.age)
# print(jackson.gender)

