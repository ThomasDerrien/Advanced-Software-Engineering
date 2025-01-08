import unittest
from src.community.domain.events.RatingCreatedEvent import RatingCreatedEvent
from src.community.domain.entities.Rating import Rating
from src.community.domain.value_objects.RatingValue import RatingValue

class TestRatingCreatedEvent(unittest.TestCase):

    def test_initialization_valid(self):
        rating_value = RatingValue(4)
        rating = Rating(id="1", value=rating_value, station_id=101, text="Good station")
        event = RatingCreatedEvent(rating)
        self.assertEqual(event.rating, rating)  # Ensure the event is correctly initialized with the rating

    def test_invalid_rating(self):
        with self.assertRaises(TypeError):
            event = RatingCreatedEvent(None)  # None should raise a TypeError

    def test_repr_method(self):
        rating_value = RatingValue(5)
        rating = Rating(id="2", value=rating_value, station_id=102, text="Excellent station")
        event = RatingCreatedEvent(rating)
        expected_repr = "RatingCreatedEvent(id=2, station_id=102,rating value=5,text=Excellent station)"
        self.assertEqual(repr(event), expected_repr)  # Ensure the repr method returns the correct string

    def test_missing_rating(self):
        with self.assertRaises(TypeError):
            event = RatingCreatedEvent(rating=None)  # Should raise a TypeError as rating can't be None

if __name__ == '__main__':
    unittest.main()
