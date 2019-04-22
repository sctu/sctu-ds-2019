#定义变量保存学生的姓名，年龄，性别
name='heyuting'
age=18
gender='male'

name2='lijuan'
age2=19
gender2='famale'

class Student:
    #构造函数
    #类里面写的函数，第一个参数都是sele
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def study(self):
        print(self.name+'studying!')

heyuting = Student('heyuting', 18, 'male')
heyuting.study()

# print(heyuting.name)
# print(heyuting.age)
# print(heyuting.gender)
#
# lijuan = Student('lijuan', 19, 'female')
# print(lijuan.name)
# print(lijuan.age)
# print(lijuan.gender)