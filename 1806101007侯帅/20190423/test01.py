#类名
# - 首字母大写
# - 切记不要使用拼音

class Computer:

    #构造函数
    def __init__(self,vender,cpu,price):
        self.vender = vender
        self.cpu = cpu
        self.price = price

        #设置参数(构造形参)
    def play_game(self):
        print("play game")



lenovo  = Computer ('asus','intel','5000.00')#构造实参

print(lenovo.cpu)
print(lenovo.vender)
print(lenovo.price)

class Infor:

    def __init__(self,height,weight,age,school,hometown):
        self.height = height
        self.weight =weight
        self.age  = age
        self.school = school
        self.hometowm =hometown

informatin= Infor('180','180','18','四川旅游学院','四川')
print(informatin.school)
print(informatin.age)
print(informatin.height)
print(informatin.weight)
print(informatin.hometowm)



