# 学生：姓名张三，年龄18，性别男

name = 'zhangsan'
age = 18
gender = 'male'

class Student:

    # 构造函数
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def printInfo(self):
        print('name: {}'.format(self.name))
        print('age: {}'.format(self.age))
        print('gender: {}'.format(self.gender))

zs = Student('zhangsan', 18, 'male');

zs.printInfo()
