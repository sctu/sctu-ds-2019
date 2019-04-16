class students:
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
