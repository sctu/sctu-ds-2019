#定义变量保存学生的姓名，年龄，性别
name = 'wang'
age = 18
gender = 'male'

a = 1
b = 2
c = 3

class Student:
    # 构造函数
    # 类里面写的函数，第一个参数都是self
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def study(self):
        print(self.name + ' studying!')
    def like(self):
        print(self.name + ' dog!')

wang = Student('wang',18,'male')
wang.study()
wang.like()

