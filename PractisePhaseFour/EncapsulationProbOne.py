class Product:
    def __init__(self,price):
        self.__price = price
    def get_price(self):
        return self.__price
    def set_price(self,value):
        if value >= 0:
            self.__price = value
        else:
            raise ValueError("Invalid Price")

prod1 = Product(10)

try:
    prod1.set_price(87)
    print(prod1.get_price())
except ValueError as e:
    print(e)