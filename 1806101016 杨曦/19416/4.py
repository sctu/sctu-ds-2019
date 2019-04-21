der = 'male'
class Student:

    #构造函数
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def printInfo(self):
        print('name:{}'.format(self.name))
        print('age:{}'.format(self.age))
        print('gender:{}'.format(self.gender))

zs = Student('zhaojiao',20,'male');
zs.printInfo()