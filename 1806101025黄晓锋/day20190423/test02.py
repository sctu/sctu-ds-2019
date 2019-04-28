class Book:
    def __init__(self,bookname,price,):
        self.bookname=bookname
        self.price=price

english=Book('English',
             '20.0')


print(english.bookname)