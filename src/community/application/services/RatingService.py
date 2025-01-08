from src.community.domain.events.RatingCreatedEvent import RatingCreatedEvent
from src.community.domain.entities.Rating import Rating
from src.community.domain.value_objects.RatingValue import RatingValue
from datetime import datetime

class RatingService:
    def __init__(self, rating_repository, charging_station_service):
        self.rating_repository = rating_repository
        self.charging_station_service = charging_station_service

    def create_rating(self, value: float, station_id: str, text: str) -> Rating:
        """
        Creates a rating for a charging station.

        :param value: Rating value (1-5)
        :param station_id: ID of the charging station being rated
        :param text: Text of the rating
        :return: The created Rating object
        """
        # Validate rating value
        if not (1 <= value <= 5):
            raise ValueError("Rating value must be between 1 and 5")

        # Validate text
        if not text:
            raise ValueError("Rating text cannot be empty")

        # Check if the station exists and is available
        station = self.charging_station_service.repository.find_by_id(station_id)
        if not station:
            raise ValueError(f"Station with ID {station_id} not found")

        # Generate a unique ID (You can use a UUID in real-world applications)
        rating_id = f"{station_id}-{datetime.now().timestamp()}"
        rating_value = RatingValue(value=value)

        # Create Rating entity
        rating = Rating(rating_id, rating_value, station_id, text)

        # Save the rating
        self.rating_repository.add(rating)

        # Trigger RatingCreatedEvent
        rating_created_event = RatingCreatedEvent(rating)
        rating_created_event.publish()

        return rating
