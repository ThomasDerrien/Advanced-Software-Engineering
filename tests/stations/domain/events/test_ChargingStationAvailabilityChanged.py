import unittest
from  src.stations.domain.events.ChargingStationAvailabilityChanged import ChargingStationAvailabilityChanged

class TestChargingStationAvailabilityChanged(unittest.TestCase):

    def test_initialization(self):
        # Test that the event is initialized correctly
        event = ChargingStationAvailabilityChanged(1, 'available', 'unavailable')

        self.assertEqual(event.station_id, 1)
        self.assertEqual(event.old_availability, 'available')
        self.assertEqual(event.new_availability, 'unavailable')

    def test_str_method(self):
        # Test that the string representation is correct
        event = ChargingStationAvailabilityChanged(1, 'available', 'unavailable')
        expected_str = "ChargingStationAvailabilityChanged: station_id=1, old_availability=available, new_availability=unavailable"

        self.assertEqual(str(event), expected_str)

    def test_empty_availability_values(self):
        # Test with empty or None availability values, should raise ValueError
        with self.assertRaises(ValueError):
            ChargingStationAvailabilityChanged(2, None, None)

        # Test with one availability value as None, should raise ValueError
        with self.assertRaises(ValueError):
            ChargingStationAvailabilityChanged(2, 'available', None)


