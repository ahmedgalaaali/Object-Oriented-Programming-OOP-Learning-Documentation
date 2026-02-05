class Product:
    def __init__(self, name, price, discount=0):
        self._name = name
        self.__price = price
        self.__discount = discount
    @property
    def name(self):
        return self._name    
    @property
    def price(self):
        return self.__price    
    @price.setter
    def price(self, value):
        if value <= 0:
            print("Price should not be zero or less!")
        else:
            self.__price = value   
    @property
    def discount(self):
        return self.__discount 
    @discount.setter
    def discount(self, value):
        if value < 0 or value > 50:
            print(f"The discount  must be between 0 and 50. You entered {value}!")
        else:
            self.__discount = value   
    @property
    def final_price(self):
        return self.__price - (self.__price * (self.__discount / 100))