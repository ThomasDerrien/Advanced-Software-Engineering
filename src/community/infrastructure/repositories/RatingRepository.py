from src.community.domain.entities.Rating import Rating
from typing import List

class RatingRepository:
    def __init__(self):
        # Initialize an in-memory store for ratings. In a real application, you would interface with a database.
        self.ratings = {}

    def add(self, rating: Rating):
        """
        Adds a new rating to the repository.

        :param rating: The Rating entity to be added.
        """
        self.ratings[rating.id] = rating

    def find_by_station_id(self, station_id: str) -> List[Rating]:
        """
        Retrieves all ratings for a specific charging station.

        :param station_id: The ID of the charging station.
        :return: List of Rating objects.
        """
        return [rating for rating in self.ratings.values() if rating.station_id == station_id]

    def find_by_id(self, rating_id: str) -> Rating:
        """
        Retrieves a rating by its ID.

        :param rating_id: The ID of the rating.
        :return: The Rating object, or None if not found.
        """
        return self.ratings.get(rating_id)

