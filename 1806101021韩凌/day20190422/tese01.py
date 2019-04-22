Class Student:
    #构造函数
    #类里面写的函数，第一个参数都是self

   def _init_(self,name,age,gender):
       self.name = name
       self.age = age
       self.gender = gender

    def _study(self):
        print(self.name+'studying')



chen = Student('chen','18','male')
print(chen,name)
print(chen.age)
print(chen.gender)