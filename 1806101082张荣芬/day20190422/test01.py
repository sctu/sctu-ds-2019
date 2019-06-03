# 定义变量保存学生的姓名，年龄，性别
name = 'zhang'
age = '18'
gender = 'female'


class student:

    # 构造函数
    # 类里面写的函数，第一个参数都是self
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def study(self):
        print(self.name + 'studying' )
    def hobby(self):
        print(self.name + '追星，小说')
    def meals(self):
        print(self.name + 'pork')


zhang = student('zhang',18,'female')
zhang.study()
zhang.hobby()
zhang.meals()
print(zhang.name,age,gender)



