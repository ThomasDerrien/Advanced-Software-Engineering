class RatingValue:
    def __init__(self, value: float):
        if not isinstance(value, (int)):
            raise TypeError("Rating value must be an int")
        if not (1 <= value <= 5):
            raise ValueError("Rating value must be between 1 and 5")
        self.value = value

    def __repr__(self):
        return f"RatingValue({self.value})"

    def is_valid(self):
        return 1 <= self.value <= 5
