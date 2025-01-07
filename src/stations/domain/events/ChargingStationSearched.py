from src.stations.domain.events.DomainEvent import DomainEvent


class ChargingStationSearched(DomainEvent):
    def __init__(self, postal_code):
        # Validate postal code is a non-empty string
        if not isinstance(postal_code, str):
            raise ValueError("Postal code must be a string.")
        if postal_code == "":
            raise ValueError("Postal code cannot be an empty string.")

        self.postal_code = postal_code

    def __str__(self):
        return f"ChargingStationSearched: postal_code={self.postal_code}"
