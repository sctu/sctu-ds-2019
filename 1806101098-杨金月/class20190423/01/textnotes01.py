#类名：  class 之后为类的名称并以冒号结尾:
    #首字母不可大写
    #不可用拼音
class Computer:
    #构造函数：对一些属性进行赋值
    #def __init__(self):


#def add():#与computer并列的函数
    #print()

   # def add(self):  # computer里面的函数
        #print()
    def __init__(self, vendor, cpu, price):
        self.vendor = vendor
        # self.vendor是类所特有的。
        self.cpu = cpu
        self.price = price

    def play_game(self):
        print('play game')

lenovo = Computer('lenovo','intel','50000.00')
#此三个参数与构造的函数的参数相匹配。

#lenovo.cpu
#有小括号表示会执行此函数

#lenovo.play_game()
#没有小括号指此为一个属性。
print(lenovo.cpu)