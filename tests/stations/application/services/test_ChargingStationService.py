import unittest
from unittest.mock import MagicMock
from src.stations.domain.events.ChargingStationSearched import ChargingStationSearched
from src.stations.domain.events.ChargingStationAvailabilityChanged import ChargingStationAvailabilityChanged
from src.stations.application.services.ChargingStationService import ChargingStationService

from src.stations.infrastructure.repositories.ChargingStationRepo import ChargingStationRepo


class TestChargingStationService(unittest.TestCase):
    def setUp(self):
        self.repository = ChargingStationRepo()
        self.repository.load_data_from_csv(r"C:\Users\INSA\Documents\GitHub\Advanced-Software-Engineering\src\shared\infrastructure\datasets\Ladesaeulenregister.csv")
        self.service = ChargingStationService(self.repository)

    def test_find_by_postal_code(self):
        # Arrange
        postal_code = 13089
        station_ids = [1570, 1571, 1572, 1573, 1574, 1575, 1576, 1577, 1578, 1579]

        # Act
        result = self.service.find_by_postal_code(postal_code)


        ids = [station.id for station in result]
        self.assertEqual(ids, station_ids)

    def test_find_available_stations(self):
        # Arrange
        available_stations = self.repository.find_all()

        # Act
        result = self.service.find_available_stations()

        # Assert
        self.assertEqual(result, available_stations)

    def test_get_all_charging_stations(self):
        # Arrange
        all_stations =  self.repository.find_all()

        # Act
        result = self.service.get_all_charging_stations()

        self.assertEqual(result, all_stations)

    def test_update_availability(self):
        station = self.repository.find_by_id(0)
        # Arrange
        old_availability = "available"
        new_availability = "unavailable"

        # Act
        self.assertEqual(station.availability.state, old_availability)

        self.service.update_availability(0, new_availability)

        # Assert
        self.assertEqual(station.availability.state, new_availability)


if __name__ == "__main__":
    unittest.main()
