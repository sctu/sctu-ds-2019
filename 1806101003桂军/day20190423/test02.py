class Computer:
    #构造函数
    def __init__(self,vender,memory,cpu):
        self.vender = vender
        self.memory = memory
        self.cpu = cpu
DELL = Computer('DELL','1T','i7')
print(DELL.memory)