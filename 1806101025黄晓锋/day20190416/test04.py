class student:

    #构造函数
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

#    def __printInfo__(self):
    #    print('name':{}.format(self.name))
   #     print('age':{}.format(self.age))
  #      print('gender':{}.format(self.gender))

zs=student('zhangsan',18,'man');

print(zs.name)

#print(age)