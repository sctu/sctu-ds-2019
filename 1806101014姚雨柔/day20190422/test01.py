# 定义变量保存学生的姓名，年龄，性别
name = 'justin'
age = 18
gender = 'male'

name2 = 'bob'
age2 = 19
gender2 = 'female'

class Student:

    # 构造函数
    # 类里面写的函数，打一个参数都是self
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def study(self):
        print(self.name + ' studying!')

chen = Student('chen', 18, 'male')
chen.study()

# print(chen.name)
# print(chen.age)
# print(chen.dender)


# bob = Student('bob', 19, 'female')
# print(bob.name)
# print(bob.age)
# print(bob.gender)

