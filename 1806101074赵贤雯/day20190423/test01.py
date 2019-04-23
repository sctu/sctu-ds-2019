#类名
# - 首字母大写
# - 切记不要使用拼音

class Computer:
    # 构造函数（名字与以前学习的函数名不同，且变量会自带self）
    def __init__(self,vendor,cpu,price):
        self.vendor = vendor
        self.cpu = cpu
        self.price = price
    def play_game(self):
        print('play game!')
lenovo = Computer('lenovo','intel','5000.00')
hp = Computer('hp','intel','7000.00')

print(lenovo.cpu)
print(hp.price)
lenovo.play_game()

class Student:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

Jed = Student('Jed', '18', 'girl')
print(Jed.gender)
'''
    def fly(self):
        print('flying')

    print(fly())
'''
# 抽象的方法是不合理的
# 必须符合客观世界的规律
# eg
