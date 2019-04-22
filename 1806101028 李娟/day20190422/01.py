#定义变量保存学生的姓名，年龄，性别
name = 'lijuan'
age = '18'
gender = 'female'

name2 = 'heyuting'
age2 = '19'
gender2 = 'male'

a = 1
b = 2
c = 3

class student:

  #构造函数
  #类里面写的函数，第一个参数都是self
  def _init_(self,name,age,gender):
    self.name = name
    self.age = age
    self.gender = gender

  def study(self):
      print(self.name + 'studying!')

lijuan = student('lijuan',18,'famle')
print(lijuan.name)
print(lijuan.age)
print(lijuan.gender)

heyuting = student('heyuting',18,'male')
print(heyuting.name)
print(heyuting.age)
print(heyuting.gender)
