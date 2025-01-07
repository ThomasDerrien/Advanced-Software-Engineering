import unittest
from unittest.mock import MagicMock
from src.stations.domain.entities.ChargingStation import ChargingStation
from src.stations.domain.value_objects.Location import Location

from src.stations.domain.value_objects.Availability import Availability

from src.stations.domain.value_objects.PostalCode import PostalCode

class TestChargingStation(unittest.TestCase):

    def test_valid_initialization(self):
        # Valid initialization test (already covered)
        station = ChargingStation(
            id=0,
            location=Location('13089', 53.0, 12.5),
            availability=Availability("available"),
            power=50.0
        )
        self.assertEqual(station.id, 0)
        self.assertEqual(station.location.postal_code.code, '13089')
        self.assertEqual(station.location.latitude, 53.0)
        self.assertEqual(station.location.longitude, 12.5)
        self.assertEqual(station.power, 50)

    def test_negative_id(self):
        # Test negative ID
        with self.assertRaises(ValueError):
            ChargingStation(
                id=-1,
                location=Location('13089', 53.0, 12.5),
                availability=Availability("available"),
                power=50.0
            )

    def test_zero_power(self):
        # Test zero power
        with self.assertRaises(ValueError):
            ChargingStation(
                id=2,
                location=Location('13089', 53.0, 12.5),
                availability=Availability("available"),
                power=0.0
            )

    def test_negative_power(self):
        # Test negative power
        with self.assertRaises(ValueError):
            ChargingStation(
                id=3,
                location=Location('13089', 53.0, 12.5),
                availability=Availability("available"),
                power=-10
            )



if __name__ == "__main__":
    unittest.main()
