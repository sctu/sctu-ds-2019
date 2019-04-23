class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('running!')

    def fly(self):
        print('flying!')


Catherine = Person('liu ', 18)
Catherine.run()