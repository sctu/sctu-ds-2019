class Computer:

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