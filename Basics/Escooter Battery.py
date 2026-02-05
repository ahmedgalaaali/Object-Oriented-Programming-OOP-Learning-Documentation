class Battery:
    def __init__(self, id, charge):
        self._id = id
        self.__charge = charge
    @property
    def id(self):
        return self._id
    @property
    def percent(self):
        return self.__charge
    @percent.setter
    def percent(self, percentage):
        if percentage <0:
            print("Battery percentage cannot be less than 0!")
        elif percentage >100:
            print("Battery percentage cannot be greater than 100!")
        else:
            self.__charge = percentage
    @property
    def remaining_range(self):
        print(f"Remaining distanceis: {self.__charge * 2.5} km!")
    def diagnostic(self):
        print("Running an quick system check... ")