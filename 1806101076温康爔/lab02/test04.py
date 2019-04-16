# 学生：姓名张三，年龄18，性别男

name:'zhangsan'
age:18
gender:male

class Student:

     # 构造函数
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.fender = gender

    def print(self):
        print('self.name{}',())
zs = Student('zhangsan', 18, 'male');

zs.name