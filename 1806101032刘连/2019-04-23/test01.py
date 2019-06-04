
class Computer:

    def __init__(self, vendor, cpu, price):
        self.vendor = vendor
        self.cpu = cpu
        self.price = price

lenovo = Computer('lenovo',
                  'intel', '5000.00')
print(lenovo.cpu)