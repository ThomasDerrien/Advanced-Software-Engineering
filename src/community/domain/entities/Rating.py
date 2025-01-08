from src.community.domain.value_objects.RatingValue import RatingValue


class Rating:
    def __init__(self, id: str, value: RatingValue, station_id: int, text: str):
        if not id or not isinstance(station_id, int):
            raise ValueError("ID cannot be empty and station_id must be an integer.")
        if not isinstance(value, RatingValue):
            raise TypeError("value must be an instance of RatingValue.")

        self.id = id
        self.ratingValue = value
        self.station_id = station_id
        self.text = text

    def is_valid(self) -> bool:
        # Ensure rating value is within a valid range (e.g., 1-5)
        if not self.ratingValue.is_valid():
            return False
        return True
