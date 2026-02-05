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

door = Smartlock(1073)
door.unlock(1000)
door.unlock(107)
door.unlock(1073)
door.change_pin(100, 2000)
door.change_pin(1073, 200)
door.change_pin(1073, 2000)
door2 = Smartlock(100)