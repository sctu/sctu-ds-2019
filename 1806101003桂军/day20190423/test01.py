#类名：
#——首字母大写
#——切记首字母大写
class Computer:
    #构造函数
    def __init__(self,vendor,cpu,price):
        self.vender = vendor
        self.cpu = cpu
        self.price = price
lenovo = Computer('lenovo','intel','5000.00')
print(lenovo.cpu)
# def __add__(self, other):
    # 函数是动词
    # 属性是名词