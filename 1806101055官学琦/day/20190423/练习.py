class Computer:
    def __init__(self,cpu,vendor,price):
        self.cpu=cpu
        self.vendor=vendor
        self.price=price

    def play_game(self):
        print("play game")

lenovo=Computer("intle","lenovo","5000")
hasee=Computer("intel","hasee","7999")
print(hasee.cpu)
lenovo.play_game()

class Dorm:
    def __init__(self,number,):
        self.number=number


dorm=Dorm("3617")
print(dorm.number)