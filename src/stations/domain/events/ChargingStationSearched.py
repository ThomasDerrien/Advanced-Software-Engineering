from DomainEvent import DomainEvent

class ChargingStationSearched(DomainEvent):
    def __init__(self, postal_code):
        self.postal_code = postal_code

    def __str__(self):
        return f"ChargingStationSearched: postal_code={self.postal_code}"

