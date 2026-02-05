class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def work(self):
        print(f"Employee {self.name} is working!")

class Manager(Employee):
    def give_speech(self):
        print(f"{self.name} is motivating the team!")

manager1 = Manager("Rania", 15000)
employee1 = Employee("Ahmed", 3500)
manager1.give_speech()
manager1.work()
employee1.work()