#类的使用
class information:
    def __init__(self,name,age,gender,sort):
        self.name=name
        self.age=age
        self.gender=gender
        self.facesort=sort
    def display(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.facesort)
zhangsan=information('zhangsan',19,'female',67)
zhangsan.display()