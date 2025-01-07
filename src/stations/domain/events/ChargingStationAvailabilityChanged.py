
from DomainEvent import DomainEvent

class ChargingStationAvailabilityChanged(DomainEvent):
    def __init__(self, station_id, old_availability, new_availability):
        self.station_id = station_id
        self.old_availability = old_availability
        self.new_availability = new_availability

    def __str__(self):
        return (
            f"ChargingStationAvailabilityChanged: station_id={self.station_id}, "
            f"old_availability={self.old_availability}, new_availability={self.new_availability}"
        )