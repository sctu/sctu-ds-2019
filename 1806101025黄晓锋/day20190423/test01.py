

#类名：
#首字母大写
#切记不能用拼音
class Computer:

    #构造函数
    def __init__(self,vendor,cup,price):
        self.vendor=vendor
        self.cpu=cup
        self.price=price

    def get_cpu(self):
        return self.cpu

    def play_game(self):
        print('play game!')

lenovo=Computer('lenov',
                'intel',
                '5000.0')
print(lenovo.price)
lenovo.cpu
lenovo.play_game()

