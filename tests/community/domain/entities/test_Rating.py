
import unittest
from src.community.domain.value_objects.RatingValue import RatingValue
from src.community.domain.entities.Rating import Rating

class TestRating(unittest.TestCase):

    def test_valid_rating(self):
        rating_value = RatingValue(4)
        rating = Rating(id="1", value=rating_value, station_id=101, text="Good station")
        self.assertTrue(rating.is_valid())

    def test_invalid_rating_value_too_low(self):
        with self.assertRaises(ValueError):
            rating_value = RatingValue(0)  # Invalid value, below valid range


    def test_invalid_rating_value_too_high(self):
        with self.assertRaises(ValueError):
            rating_value = RatingValue(6)  # Invalid value, below valid range

    def test_missing_id(self):
        rating_value = RatingValue(3)
        with self.assertRaises(ValueError):
            rating = Rating(id="", value=rating_value, station_id=104, text="Average station")

    def test_invalid_station_id_type(self):
        rating_value = RatingValue(4)
        with self.assertRaises(ValueError):
            rating = Rating(id="5", value=rating_value, station_id="station_105", text="Invalid station ID")

    def test_null_rating_value(self):
        with self.assertRaises(TypeError):
            rating = Rating(id="7", value=None, station_id=107, text="No rating value")

    def test_null_text(self):
        rating_value = RatingValue(2)
        rating = Rating(id="8", value=rating_value, station_id=108, text=None)
        self.assertTrue(rating.is_valid())  # Assuming None text is acceptable

    def test_invalid_rating_value_type(self):
        with self.assertRaises(TypeError):
            rating_value = "invalid_rating"  # Invalid type, not RatingValue
            rating = Rating(id="9", value=rating_value, station_id=109, text="Invalid rating type")

if __name__ == '__main__':
    unittest.main()
