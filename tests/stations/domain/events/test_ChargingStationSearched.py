import unittest
from src.stations.domain.events.ChargingStationSearched import ChargingStationSearched

class TestChargingStationSearched(unittest.TestCase):

    def test_initialization(self):
        # Test with a valid postal code
        event = ChargingStationSearched(12345)
        self.assertEqual(event.postal_code, 12345)

    def test_str_method(self):
        # Test the string representation
        event = ChargingStationSearched(12345)
        expected_str = "ChargingStationSearched: postal_code=12345"
        self.assertEqual(str(event), expected_str)


    def test_none_postal_code(self):
        # Test with None as postal code, should raise ValueError
        with self.assertRaises(ValueError):
            ChargingStationSearched(None)

    def test_invalid_postal_code_type(self):
        # Test with an invalid postal code type, should raise ValueError
        with self.assertRaises(ValueError):
            ChargingStationSearched("12345")  # string instead of integer

        with self.assertRaises(ValueError):
            ChargingStationSearched([12345])  # List instead of string

