from domain.events.ChargingStationSearched import ChargingStationSearched
from domain.events.ChargingStationAvailabilityChanged import ChargingStationAvailabilityChanged

class ChargingStationService:
    def __init__(self, repository):
        self.repository = repository  


    def find_by_postal_code(self, postal_code):
        """
        Finds all charging stations in a specific postal code.

        :param postal_code: PostalCode object to filter stations by
        :return: List of ChargingStation objects
        """
        result = self.repository.find_by_postal_code(postal_code)
        ChargingStationSearched(postal_code).publish()
        return result

    def find_available_stations(self):
        """
        Finds all available charging stations.

        :return: List of ChargingStation objects
        """
        return self.repository.find_available()
    
    def get_all_charging_stations(self):
        return self.repository.find_all()
    
    def update_availability(self, station_id, new_availability):
        """
        Updates the availability of a charging station and triggers an event.

        :param station_id: ID of the station to update
        :param new_availability: New Availability object
        """
        station = self.repository.find_by_id(station_id)
        if station:
            old_availability = station.availability
            station.availability = new_availability
            ChargingStationAvailabilityChanged(station_id, old_availability, new_availability).publish()
