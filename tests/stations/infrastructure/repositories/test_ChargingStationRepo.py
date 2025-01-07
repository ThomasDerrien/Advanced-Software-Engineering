import unittest
from src.stations.domain.entities.ChargingStation import ChargingStation
from src.stations.domain.value_objects.Location import Location
from src.stations.domain.value_objects.PostalCode import PostalCode
from src.stations.domain.value_objects.Availability import Availability
from src.stations.infrastructure.repositories.ChargingStationRepo import ChargingStationRepo
import pandas as pd
from unittest.mock import patch

class TestChargingStationRepo(unittest.TestCase):

    def setUp(self):
        # Create a ChargingStationRepo instance for testing
        self.repo = ChargingStationRepo()

        # Create sample ChargingStation data for testing
        location1 = Location(postal_code='10115', latitude=52.5200, longitude=13.4050)
        location2 = Location(postal_code='14199', latitude=52.5000, longitude=13.4000)
        availability1 = Availability("available")
        availability2 = Availability("unavailable")
        station1 = ChargingStation(id=1, location=location1, availability=availability1, power=50.0)
        station2 = ChargingStation(id=2, location=location2, availability=availability2, power=100.0)

        self.repo.add(station1)
        self.repo.add(station2)

    def test_add_charging_station(self):
        # Test adding a ChargingStation
        location = Location(postal_code='10115', latitude=52.5300, longitude=13.5050)
        availability = Availability("available")
        new_station = ChargingStation(id=3, location=location, availability=availability, power=75.0)

        self.repo.add(new_station)
        self.assertEqual(len(self.repo.find_all()), 3)  # Should have 3 stations

    def test_remove_charging_station(self):
        # Test removing a ChargingStation by ID
        self.repo.remove(1)
        self.assertEqual(len(self.repo.find_all()), 1)  # Should have 1 station left

    def test_find_by_id(self):
        # Test finding a ChargingStation by ID
        station = self.repo.find_by_id(1)
        self.assertIsNotNone(station)
        self.assertEqual(station.id, 1)

        # Test finding a non-existent station
        station = self.repo.find_by_id(999)
        self.assertIsNone(station)

    def test_find_by_postal_code(self):
        # Test finding ChargingStations by postal code
        stations = self.repo.find_by_postal_code('10115')
        self.assertEqual(len(stations), 1)  # Should return 1 station for postal code '10115'
        self.assertEqual(stations[0].location.postal_code.code, '10115')

        stations = self.repo.find_by_postal_code('14199')
        self.assertEqual(len(stations), 1)  # Should return 1 station for postal code '14199'

        stations = self.repo.find_by_postal_code('99999')
        self.assertEqual(len(stations), 0)  # Should return 0 stations for an invalid postal code

    def test_find_available(self):
        # Test finding available ChargingStations
        available_stations = self.repo.find_available()
        self.assertEqual(len(available_stations), 1)  # Only 1 station should be available

    @patch('pandas.read_csv')
    def test_load_data_from_csv(self, mock_read_csv):
        # Test loading data from CSV using mock data
        mock_data = {
            'Postleitzahl': [10115, 14199],
            'Breitengrad': [52.00, 53.000],
            'Längengrad': [13.0, 17.000],
            'Nennleistung Ladeeinrichtung [kW]': [50.0, 100.0],
            'Bundesland': ['Berlin', 'Berlin']
        }
        mock_df = pd.DataFrame(mock_data)
        mock_read_csv.return_value = mock_df

        # Call the load_data_from_csv method
        self.repo.load_data_from_csv('mock_file.csv')

        # Verify that data was added to the repository
        self.assertEqual(len(self.repo.find_all()), 4)  # 4 stations should be in the repo (2 initial + 2 loaded from CSV)

    def test_add_station_at_existing_location(self):
        # Test adding a ChargingStation at a location where one already exists
        location = Location(postal_code='10115', latitude=52.5200, longitude=13.4050)
        availability = Availability("available")
        new_station = ChargingStation(id=3, location=location, availability=availability, power=75.0)

        # Try adding the station at an existing location
        with self.assertRaises(ValueError) as context:
            self.repo.add(new_station)

        self.assertEqual(str(context.exception), "A ChargingStation already exists at this location.")


if __name__ == '__main__':
    unittest.main()
