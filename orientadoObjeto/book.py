class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price
        self.earns = quantity*price
        self.__discount = None

    def set_discount(self, discount):
        self.__discount = discount

    def get_price(self):
        if self.__discount: 
            priceDisc = self.price - (self.price * self.__discount/100) 
            return priceDisc

    def __repr__(self):
        return 'O valor atualizado com o desconto é de: ' + str(self.get_price())

book1=Book('Guerra e Paz', 10, 'Tolstoi', 59.90)
book1.set_discount(30)
print(book1.get_price())