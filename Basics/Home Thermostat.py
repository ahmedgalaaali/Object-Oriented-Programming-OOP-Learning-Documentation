from datetime import datetime
class Thermostat:
    def __init__(self, serial_number, current_temp):
        self._serial_number = serial_number
        self.__current_temp = current_temp
    
    @property
    def serial_number(self):
        print(f"Action time: {datetime.now()}")
        return self._serial_number
    
    @property
    def temp(self):
        return self.__current_temp
    
    @temp.setter
    def temp(self, value):
        if value < 10:
            print("Temprature cannot be set less that 10 °C!")
        elif value > 30:
            print("Temprature cannot be set greater that 30 °C!")
        else:
            self.__current_temp = value

home1 = Thermostat(987987000, 22)

print(home1.serial_number)

print(home1.temp)

home1.temp = 17

print(f"{home1.temp}°C" )