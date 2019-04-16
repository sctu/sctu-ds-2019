#学生：姓名  张三  年龄18   性别男



name="侯帅"
age=18
gender='男性'
code='007'


class Student:

    #构造函数
    def __init__(self,name,age,gender,code):
        self.name = name
        self.age = age
        self.gender = gender
        self.code =code

    def printInfo(self):
        print('name: {}'.format(self.name))
        print('age: {}'.format(self.age))
        print('gender: {}'.format(self.gender))
        print('code:{}'.format(self.code))


zs = Student('侯帅',18,'男性','007');
zs.printInfo()
