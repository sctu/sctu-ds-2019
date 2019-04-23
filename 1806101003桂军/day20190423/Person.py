class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def run(self):
        print('running!')
        #抽象的方法是不合理的。
        #必须符合客观世界的规律
    def fly(self):
        print('flying!')
