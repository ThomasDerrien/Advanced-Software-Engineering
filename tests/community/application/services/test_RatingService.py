import unittest
from unittest.mock import MagicMock
from src.community.domain.entities.Rating import Rating
from src.community.application.services.RatingService import RatingService


class TestRatingService(unittest.TestCase):

    def setUp(self):
        # Mocking dependencies
        self.rating_repository = MagicMock()
        self.charging_station_service = MagicMock()
        self.service = RatingService(self.rating_repository, self.charging_station_service)

    def test_create_valid_rating(self):
        # Mock a valid station
        station_id = 123
        self.charging_station_service.repository.find_by_id.return_value = MagicMock(id=station_id)
        rating_value = 4
        text = "Great station!"

        rating = self.service.create_rating(value=rating_value, station_id=station_id, text=text)

        # Check that the rating was created correctly
        self.assertIsInstance(rating, Rating)
        self.assertEqual(rating.ratingValue.value, rating_value)
        self.assertEqual(rating.station_id, station_id)
        self.assertEqual(rating.text, text)

        # Ensure the rating is saved
        self.rating_repository.add.assert_called_once_with(rating)


    def test_invalid_rating_value(self):
        # Test invalid rating value below 1
        with self.assertRaises(ValueError):
            self.service.create_rating(value=0, station_id="123", text="Bad station")

        # Test invalid rating value above 5
        with self.assertRaises(ValueError):
            self.service.create_rating(value=6, station_id="123", text="Excellent station")

    def test_non_existing_station(self):
        # Mock non-existing station
        self.charging_station_service.repository.find_by_id.return_value = None
        with self.assertRaises(ValueError):
            self.service.create_rating(value=3, station_id="999", text="Station not found")

    def test_missing_text(self):
        # Test missing text
        with self.assertRaises(ValueError):
            self.service.create_rating(value=3, station_id="123", text="")


if __name__ == '__main__':
    unittest.main()
