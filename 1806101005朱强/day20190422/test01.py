#定义变量保存学生的姓名，年龄，性别
name='lizhikui'
age=18
gender='male'

name2='zhuqiang'
age2=19
gender2='female'

ss Student:
#构造函数
#类里面写的函数，第一个参数都是self
def_init_(self,name,age,gender):
self.name=name
self.age=age
self.gender=gender

chen=Student('chen',18,'male')
print(chen.name)
print(chen.age)
print(chen.gender)
bob=Student('bob',19,'male')
print(bob.name)
print(bob.age)
print(bob.gender)


