
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('running!')

    # ����ķ����ǲ�����ġ�
    # ������Ͽ͹�����Ĺ���
    def fly(self):
        print('flying!')


justin = Person('chen', 18)
justin.run()