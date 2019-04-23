
#类名首字母大写
#切记不要使用拼音
class students:
    #构造函数
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printinfo(self):
        print("name:{}".format(self.name))
        print("age:{}".format(self.age))
        print("gender:{}".format(self.gender))

zs=students("zhangsan",18,"male")
zs.printinfo()

