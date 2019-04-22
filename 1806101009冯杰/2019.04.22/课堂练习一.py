# coding: utf-8
#定义变量保存学生的姓名，年龄，性别
name = "justin"
age = 18
gender = 'male'
a = 1
b = 2
c = 3


class Student:

    #构造函数
    #类里面的函数，第一个参数都是self
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def study(self):

        print(self.name + 'stydying!')

feng = Student('feng', 18, 'male')
feng.study()





#feng = Student('feng',18,'male')
#print(feng.name)
#print(feng.age)
#print(feng.gender)
