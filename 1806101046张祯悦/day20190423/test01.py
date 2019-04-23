class Computer:
    #构造函数
    def __init__(self,vendor,cpu,price):
        self.vendor = vendor
        self.cpu = cpu
        self.price = price

lenovo = Computer('lenovo',
                  'intel','5000.00')
print(lenovo.cpu)

     def play_game(self):
         print('play game!')

lenovo = Computer('lenovo',
                  'intel','5000.00')
print(lenovo.play_game)

     def classroom(self):
         print('')