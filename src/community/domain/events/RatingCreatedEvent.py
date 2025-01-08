from src.community.domain.events.DomainEvent import DomainEvent
from src.community.domain.entities.Rating import Rating

class RatingCreatedEvent(DomainEvent):
    def __init__(self, rating: Rating):
        if not isinstance(rating, Rating):
            raise TypeError("The event must be initialized with a valid Rating object")
        self.rating = rating

    def __repr__(self):
        return f"RatingCreatedEvent(id={self.rating.id}, station_id={self.rating.station_id},rating value={self.rating.ratingValue.value},text={self.rating.text})"
