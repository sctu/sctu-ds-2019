class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('running!')

    # 抽象的方法是不合理的
    # 必须遵循客观实际规律
    def fly(self):
        print('flying!')

Allen = Person('deng', 27)
Allen.run()
