
# 类名：
# - 类的首字母大写（每一个单词）
# - 切记不要使用拼音（任何时候）

class Computer:
    #构造函数
    def __init__(self, vendor, cpu, price):
        self.vender = vendor
        self.cpu = cpu
        self.price = price

    def play_game(self):
        print('play game!')

    def get_cpu(self):
        return self.cpu

hp = Computer('hp', 'intel', '6000.00')
print(hp.cpu)

hp.cpu
hp.play_game()






