# Object-Oriented-Programming-OOP-Learning-Documentation

This repository documents my journey mastering Object-Oriented Programming in Python. Below are the core concepts I have implemented, ranging from the four fundamental pillars to Python-specific philosophies like "Consenting Adults" and property decorators.
## Content:
* [The main four pillars of OOP](#the-main-four-pillars-of-oop)
    1. [Encapuslation](#1-encapuslation)
        - [Protected vs Private attributes](#protected-vs-private-attributes)
        - [Getters and Setters](#getters-and-setters)
    2. [Abstraction](#2-abstraction)
    3. [Inheritance](#3-inheritance)
    4. [Polymorphism](#4-polymorphism)
* [Dunder Methods](#dunder-methods)

## The main four pillars of OOP
### 1. Encapuslation
Encapsulation is the practice of hiding the internal implementation of a class. Its primary goal is to expose only the important functionality to the outside world.
In my implementation, I utilized protected methods inside classes to create higher-level functional methods. This ensures the user can interact with the software without needing to be informed about the underlying implementation details.

In the example below, a minor system was created for a smart door lock:

```python
class Smartlock:
    def __init__(self, pin):
        if len(str(pin)) != 4:
            raise ValueError("PIN must be 4 digits!")
        else: self.__pin = pin
    def unlock(self, pin_check):
        if pin_check == self.__pin:
            print("Click! Door Unlocked.")
        else:
            print("Access Denied!")
    def change_pin(self, old_pin, new_pin):
        if old_pin != self.__pin:
            print("You entered wrong PIN! Try again to change the PIN!")
        elif len(str(new_pin)) != 4:
            print("PIN must be 4 digits!")
        else:
            self.__pin = new_pin
            print("PIN changed successfully!")
```
- Class name `SmartLock`
- The class accepts an initial input `pin`, the default PIN.
- The reason behind making `self.__pin` **private** is that nobody tries to edit the initial PIN with a direct code ex. `pin = 0000`
- **Methods** here are the **actions**
---
#### **Protected vs Private attributes**

| Feature | Protected Attributes | Private Attributes |
| :--- | :--- | :--- |
| **Syntax Example** | `_email` | `__email`  |
| **Accessibility** | If mentioned outside the class, they **can be returned**. | Python **will not return the values** even if the attribute is mentioned correctly. |
| **Mechanism** | The "protected variable role" **should be respected** by the developer, even though access is technically possible. | Python changes the name internally (**name mangling**) so that they cannot be accessed directly. |
| **Definition** | Attributes that are intended to be accessed only inside the class. | "Same as protected" regarding intent, but Python enforces the restriction strictly. |
---
#### **Getters and Setters**
| Feature | Getters | Setters |
| :--- | :--- | :--- |
| **Decorator Syntax** | `@property`| `@age.setter` (e.g., `@variable.setter`) |
| **Role** | Identified in the notes simply as the **getter**. | Identified in the notes simply as the **setter**. |
| **Philosophy** | Part of the "pythonic way" that gives you "more controle over the code". | Allows you to "add more code to the class, while the attributes are still private". |
| **How to call** | `Class().getter_name` | `setter_name = target value` |
---
### 2. Abstraction
Abstraction is closely linked to Encapsulation. **In my notes**, I defined Encapsulation as the mechanism used to support Abstraction. By hiding internal functionality, we achieve a level of abstraction that simplifies the interface for the user.
```python
import time
class barista:
    def make_coffee(self):
        print("Your coffee is being prepared!")
        def __grind_beans():
            pass
        time.sleep(3)
        print("Beans grinded!")
        def __boil_water():
            pass
        time.sleep(3)
        print("Water boiled!")
        def __pour_into_cup():
            pass
        time.sleep(3)
        print("Your coffee is ready!")
```
---

#### **Private methods** (`__grind_beans()`...)
Private same as private attributes, private methods are only created to be accessible inside the class itself, which supports the definition of absstraction pretty well. When `make_coffee()` is called, **the method runs three different methods/actions in the background**, while the user only called one single action to be made which is a *cup of coffee*.

---

### 3. Inheritance
Inheritance allows for the creation of new classes based on existing classes. This establishes a hierarchical relationship between the **superclass** (parent) and the **subclass** (child).

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def work(self):
        print(f"Employee {self.name} is working!")

class Manager(Employee):
    def give_speech(self):
        print(f"{self.name} is motivating the team!")
```

While **managers** are also **employees**, only managers are allowed to give speeches to other employees.

---

### 4. Polymorphism
Polymorphism allows objects of different classes to be treated as objects of a common superclass. It is the ability to use a common interface for multiple forms (data types). Practically, this often means defining methods in the child class that have the same name as methods in the parent class (Method Overriding), allowing the child class to implement the method in its own specific way.

```python
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
```

## Dunder methods
