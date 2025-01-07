from src.stations.domain.value_objects.Location import Location

from src.stations.domain.value_objects.Availability import Availability
class ChargingStation:
    def __init__(self, id, location, availability, power):
        if not isinstance(id, int) or id < 0:
            raise ValueError("ID must be a non-negative integer.")
        self.id = id
        if not isinstance(location, Location):
            raise TypeError("Location must be a valid Location object.")
        self.location = location
        if not isinstance(availability, Availability):
            raise TypeError("availability must be a valid Availability object.")
        self.availability = availability
        if not isinstance(power, float) or power <= 0:
            raise ValueError("Power must be a positive integer.")
        self.power = power

    @property
    def is_available(self)->bool:
        return self.availability.is_available()