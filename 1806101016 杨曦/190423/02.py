class Person:

    def __init__(self , name , age):      #类，和参数一般是动词
        self.name = name
        self.age = age

    def run(self):               #函数一般是动词开头
        print('runing!')
        #抽象的方法是不合理的。
        #必须符合客观世界规律

    def fly(self):
        print('flying')

justin = Perosn('yang',19)
justin .run
