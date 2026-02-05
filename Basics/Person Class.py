class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
   
    def greet(self):
        print(f"Hello World, my name is {self.name} and my age is {self.age} years old!")

person1 = Person("Alice", 30)
person1. greet()

person2 = Person("Bob", 32)
person2.greet()