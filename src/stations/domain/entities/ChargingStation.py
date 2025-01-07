class ChargingStation:
    def __init__(self, id, location, availability, power):
        self.id = id
        self.location = location
        self.availability = availability
        self.power = power

    @property
    def is_available(self)->bool:
        return self.availability.is_available()