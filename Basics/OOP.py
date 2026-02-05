class Test:
    def __init__(self, name, type):
        self.name = name
        self.type = type
    def __repr__(self):
        return f"Pokemon(name='{self.name}', type='{self.type}')"

x = Test("Ahmed", "Human")
y = Test("Basma", "Cat")

list = [x,y]
print(list)