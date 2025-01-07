import unittest
from src.stations.domain.value_objects.Location import Location

class TestLocation(unittest.TestCase):

    def test_valid_location(self):
        # Valid location with correct postal code, latitude, and longitude
        valid_location = Location('10115', 52.5200, 13.4050)  # Berlin coordinates
        self.assertEqual(valid_location.postal_code.code, '10115')
        self.assertEqual(valid_location.latitude, 52.5200)
        self.assertEqual(valid_location.longitude, 13.4050)

    def test_invalid_postal_code(self):
        # Invalid postal code
        with self.assertRaises(ValueError):
            Location('9999', 52.5200, 13.4050)  # Invalid postal code

    def test_invalid_latitude_range(self):
        # Latitude outside valid range (-90 to 90)
        with self.assertRaises(ValueError):
            Location('10115', -91.0, 13.4050)  # Latitude too low

        with self.assertRaises(ValueError):
            Location('10115', 91.0, 13.4050)  # Latitude too high

    def test_invalid_longitude_range(self):
        # Longitude outside valid range (-180 to 180)
        with self.assertRaises(ValueError):
            Location('10115', 52.5200, -181.0)  # Longitude too low

        with self.assertRaises(ValueError):
            Location('10115', 52.5200, 181.0)  # Longitude too high

    def test_location_equality(self):
        # Testing equality of Location objects
        loc1 = Location('10115', 52.5200, 13.4050)
        loc2 = Location('10115', 52.5200, 13.4050)
        loc3 = Location('14199', 52.5200, 13.4050)
        self.assertTrue(loc1 == loc2)  # Should be equal
        self.assertFalse(loc1 == loc3)  # Should not be equal

    def test_location_string_representation(self):
        # Testing string representation of Location object
        loc = Location('10115', 52.5200, 13.4050)
        self.assertEqual(str(loc), '10115, (52.52, 13.405)')

if __name__ == '__main__':
    unittest.main()
