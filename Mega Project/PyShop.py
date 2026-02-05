class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price
    def get_price(self):
        return self.__price
    def product_name(self):
        return self.name

class Physical(Product):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.__weight = weight
    def get_total_cost(self):
        return (self.__weight * 5) + self.get_price()

class Digital(Product):
    def __download_link():
        print("Click here to download!")
    def get_total_cost(self):
        return self.get_price()

class Customers:
    def __init__(self, name, email, credit_card):
        self.__name = name
        self.__email = email
        self.__credit_card = credit_card
    def masked_card(self):
        return f"****-{self.__credit_card[-4:]}"
    def get_customer_name(self):
        return self.__name
    def get_email(self):
        return self.__email
    
class Order:
    def __init__(self, customer_info):
        self.cart = []
        self.__customer_info = customer_info
    def add_to_cart(self, order):
        self.cart.append(order)
    def checkout(self):
        print(f'''
------------------------
Your reciept is ready!
------------------------
''')
        print(f'''
------------------------
User Information:
------------------------
Name: {self.__customer_info.get_customer_name()}
Email: {self.__customer_info.get_email()}
Card used: {self.__customer_info.masked_card()}
''')
        print(f'''
------------------------
Reciept:
------------------------
''')        
        for item in self.cart:
            print(f"{item.product_name()}: {item.get_total_cost()}EGP")

        print(f'''
------------------------
Grand Total: {sum(i.get_price() for i in self.cart)}EGP
------------------------
''')

order01122026 = Order(Customers("Ahmed", "ahmedgalaa4@gmail.com", "1234567890123456"))
order01122026.add_to_cart(Physical("Keyboard", 850, 0.9))
order01122026.add_to_cart(Physical("Mouse", 250, 0.2))
order01122026.add_to_cart(Digital("Ebook", 1000))
order01122026.add_to_cart(Digital("Ghost of Tsushima", 3000))
order01122026.checkout()
