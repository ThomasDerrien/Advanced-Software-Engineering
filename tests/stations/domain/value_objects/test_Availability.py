import unittest
from src.stations.domain.value_objects.Availability import Availability

class TestAvailability(unittest.TestCase):

    def test_valid_state_available(self):
        availability = Availability("available")
        self.assertTrue(availability.is_available())

    def test_valid_state_unavailable(self):
        availability = Availability("unavailable")
        self.assertFalse(availability.is_available())

    def test_valid_state_maintenance(self):
        availability = Availability("maintenance")
        self.assertFalse(availability.is_available())

    def test_invalid_state(self):
        with self.assertRaises(ValueError):
            Availability("invalid_state")

    def test_case_insensitive_state(self):
        availability = Availability("AVAILABLE")
        self.assertTrue(availability.is_available())

        availability = Availability("UnAvAiLaBlE")
        self.assertFalse(availability.is_available())

    def test_equality_same_state(self):
        availability1 = Availability("available")
        availability2 = Availability("available")
        self.assertEqual(availability1, availability2)

    def test_equality_different_state(self):
        availability1 = Availability("available")
        availability2 = Availability("maintenance")
        self.assertNotEqual(availability1, availability2)

    def test_equality_with_different_type(self):
        availability = Availability("available")
        self.assertNotEqual(availability, "available")

    def test_str_method(self):
        availability = Availability("available")
        self.assertEqual(str(availability), "available")

        availability = Availability("maintenance")
        self.assertEqual(str(availability), "maintenance")


if __name__ == "__main__":
    unittest.main()
