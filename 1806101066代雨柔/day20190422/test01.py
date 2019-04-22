# -*- coding: UTF-8 -*-
#定义变量保存学生的姓名、年龄、性别
name='dai'
age=18
gender='male'
class Student:
    #构造函数
    #在类里面第一个写的函数，第一个参数都是self
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def study(self):
        print (self.name + 'studying!')
dai=Student('dai',18,'gender')
dai.study()

# print(dai.name)
# print(dai.age)
# print(dai.gender)


name='jeson'
age=37
gender='male'
class Singer:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def hobby(self):
        print(self.name + 'singing!')
jeson = Singer('jeson', 37, 'male')
jeson.hobby()
 #print(jeson.name)
 #print(jeson.age)
 #print(jeson.gender)



