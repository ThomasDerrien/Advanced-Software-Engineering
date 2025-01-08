import unittest
from src.community.domain.entities.Rating import Rating
from src.community.domain.value_objects.RatingValue import RatingValue
from src.community.infrastructure.repositories.RatingRepository import RatingRepository

class TestRatingRepository(unittest.TestCase):

    def setUp(self):
        self.repository = RatingRepository()

    def test_add_and_find_by_id(self):
        # Create and add a rating
        rating_value = RatingValue(4)
        rating = Rating(id="1", value=rating_value, station_id=123, text="Great station!")
        self.repository.add(rating)

        # Retrieve the rating by its ID
        retrieved_rating = self.repository.find_by_id("1")
        self.assertEqual(retrieved_rating, rating)

        # Check retrieval of a non-existent ID
        self.assertIsNone(self.repository.find_by_id("2"))

    def test_find_by_station_id(self):
        # Add multiple ratings for different stations
        rating1 = Rating(id="1", value=RatingValue(4), station_id=123, text="Great station!")
        rating2 = Rating(id="2", value=RatingValue(5), station_id=123, text="Excellent station!")
        rating3 = Rating(id="3", value=RatingValue(3), station_id=456, text="Good but could be better.")
        self.repository.add(rating1)
        self.repository.add(rating2)
        self.repository.add(rating3)

        # Retrieve ratings by station ID
        station_123_ratings = self.repository.find_by_station_id(123)
        self.assertEqual(station_123_ratings, [rating1, rating2])

        # Ensure only relevant ratings are returned
        station_456_ratings = self.repository.find_by_station_id(456)
        self.assertEqual(station_456_ratings, [rating3])

        # Check for a station ID with no ratings
        station_789_ratings = self.repository.find_by_station_id(789)
        self.assertEqual(station_789_ratings, [])

    def test_empty_repository(self):
        # Query an empty repository
        self.assertIsNone(self.repository.find_by_id("1"))
        self.assertEqual(self.repository.find_by_station_id(123), [])

if __name__ == '__main__':
    unittest.main()
