# 类名：
# - 首字母大写
# - 切记不要使用拼音
class Computer:
    #构造函数

    def  __index__(self):

        print()

    def __add__(self , vendor , cpu , price):        #括号里的参数
        self.vendor = vendor
        self.cpu = cpu
        self.price = price
    def play_game(self):              #变量，保存在类里面
        print('paly_game!')


dell = Computer('dell',
                  'inrel','7000,00')       #对应的参数    与构造函数里的参数是对应的
dell.cpu#属性
dell.play_game()#未完成，结束的函数

print(dell.cpu)
