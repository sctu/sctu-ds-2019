#定义变量保存学生的姓名，年级，性别
name = "wangrui"
age = 20
gender = "male"
name2 = "bob"
age2 = 19
gender2 = "female"

class  Student:
    # 下划线表示构造函数,类里面写的函数，第一个参数都是self
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def study(self):
        print(self.name + "studying!")
    def habbit(self):
        print(self.name + "读书看报")
    def speciality(self):
        print(self.name + "吃饭睡觉")

wang = Student("wang",20,"male")

wang.study()
wang.habbit()
wang.speciality()

print(wang.name,age,gender)
print(name2,age2,gender2)




