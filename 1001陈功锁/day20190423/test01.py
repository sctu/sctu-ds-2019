# 类名：
# - 首字母大写
# - 切记不要使用拼音
class Computer:

    # 构造函数
    def __init__(self, vendor, cpu, price):
        self.vendor = vendor
        self.cpu = cpu
        self.price = price

    def play_game(self):
        print('play game!')


lenovo = Computer('lenovo',
                  'intel', '5000.00')
lenovo.cpu
lenovo.play_game()
