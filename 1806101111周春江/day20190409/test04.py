name = 'zhangsan'
age = 18
gender = 'male'
class Student:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def printInfo(self):
        print('name:{}'.format(self,name))
        print('age:{}'.format(self,age))
        print('gender:{}'.format(self,gender))
zs = Student('zhangsan',18,'male');
