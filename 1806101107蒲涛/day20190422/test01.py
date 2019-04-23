#定义变量 保存学生的 姓名 年龄 性别
# a=print(input(eval('please enter your name:')))   ?????????????
# -*- coding: UTF-8 -*-


class Student:


    # 构造函数
    # 类里面写的函数，第一个参数都是self
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def learn(self):
        print(self.name+'learning!')

tao=Student('tao',18,'male')
tao.learn()
# print(tao.name)
# print(tao.age)
# print(tao.sex)
#
# bob=Student('bob',19,'female')
# print(bob.name)
# print(bob.age)
# print(bob.sex)

