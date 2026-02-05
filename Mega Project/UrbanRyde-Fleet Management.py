class vehicles:
    def __init__(self, liscense_plate, odometer):
        self.__liscence_plate = liscense_plate
        self.__odometer = odometer
    @property
    def liscence(self):
        return f"Liscence plate: {self.__liscence_plate}"
    @property
    def odometer(self):
        return f"Total unit:{self.__odometer}km"

class StandardCars(vehicles):
    def fare(self, unit):
        self.__unit = unit
        return self.__unit * 2
    @property
    def distance(self):
        print(f"Total unit: {self.__unit}")

class LuxurySUVs(vehicles):
    def fare(self, unit):
        self.__unit = unit
        return (self.__unit * 4) + 10
    @property
    def distance(self):
        print(f"Total distance: {self.__unit}")

class Escooter(vehicles):
    def __init__(self, liscense_plate, odometer):
        super().__init__(liscense_plate, odometer)
        self.base_charge = 100
    def fare(self, unit):
        self.__unit = unit
        return self.__unit * 0.5
    
class FleetManager:
    def __init__(self):
        self.__fleet = []
        self.__total_revenue = 0
    def view_vehicles(self):
        return self.__fleet
    def add_vehicle(self, vehicle):
        self.__fleet.append(vehicle)
        print(f"{vehicle} was added to the fleet!")
    def rent_vehicle(self, index, amount):
        self.index = index
        self.amount = amount
        selected_vehicle = self.__fleet[index]
        amount_spent = selected_vehicle.fare(amount)
        self.__total_revenue += amount_spent
        print(f'''
----------------------------------------------- \n
Successful transaction! \n
Vehicle selected: {selected_vehicle.liscence}\n
Trip charged: {amount_spent}$ \n
Company's total revenue: {self.__total_revenue} \n
-----------------------------------------------
        ''')

manager = FleetManager()
manager.add_vehicle(StandardCars("XYZ2010", 50000))
manager.rent_vehicle(0, 20)