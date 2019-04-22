# -*- coding: UTF-8 -*-
# 定义变量保存学生的姓名，年龄，性别

name = '李国银'
age = '19'
gender = 'male'


class  Student:

    # init 是构造函数
    # 在类里面写的函数，第一个参数都是self
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def study(self):
        print(self.name)

    def hobby(self):
        print(self.name + '  does well in Cross Fire!')

    def like(self):
        print(self.name + '  likes blue,red,green and yellow!')

    def sleep(self):
        print(self.name + '  sleeps at eleven o’clock!')

li = Student('李国银','19','male')
li.study()
li.hobby()
li.like()
li.sleep()


# print(chen.name)
# print(chen.age)
# print(chen.gender)
