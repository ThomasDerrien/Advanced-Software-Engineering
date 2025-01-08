import unittest
from src.community.domain.value_objects.RatingValue import RatingValue

class TestRatingValue(unittest.TestCase):

    def test_valid_rating(self):
        rating_value = RatingValue(4)
        self.assertEqual(rating_value.value, 4)  # Ensure the value is correctly assigned
        self.assertTrue(rating_value.is_valid())

    def test_invalid_rating_value_below_1(self):
        with self.assertRaises(ValueError):
            RatingValue(0)  # Value should be between 1 and 5

    def test_invalid_rating_value_above_5(self):
        with self.assertRaises(ValueError):
            RatingValue(6)  # Value should be between 1 and 5

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            RatingValue("five")  # Non-numeric input should raise an error

    def test_edge_case_value_1(self):
        rating_value = RatingValue(1)
        self.assertTrue(rating_value.is_valid())  # 1 is a valid rating value

    def test_edge_case_value_5(self):
        rating_value = RatingValue(5)
        self.assertTrue(rating_value.is_valid())  # 5 is a valid rating value

    def test_repr_method(self):
        with self.assertRaises(TypeError):
            rating_value = RatingValue(3.5)

    def test_is_valid_method_valid(self):
        rating_value = RatingValue(2)
        self.assertTrue(rating_value.is_valid())  # 2 should be valid

    def test_is_valid_method_invalid(self):
        rating_value = RatingValue(5)
        rating_value.value+=1
        self.assertFalse(rating_value.is_valid())  # 6 should not be valid

if __name__ == '__main__':
    unittest.main()
