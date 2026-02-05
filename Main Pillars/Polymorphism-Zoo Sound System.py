class Lion:
    def speak(self):
        print("ROAR!")

class Duck:
    def speak(self):
        print("Quack!")

class Dog:
    def speak(self):
        print("Whoof Whoof!")

animals = [Lion(), Duck(), Dog()]

for animal in animals:
    animal.speak()