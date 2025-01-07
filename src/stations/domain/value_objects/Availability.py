class Availability:
    VALID_STATES = {"available", "unavailable", "maintenance"}

    def __init__(self, state):
        if state.lower() not in self.VALID_STATES:
            raise ValueError(f"Invalid availability state. Must be one of {self.VALID_STATES}.")
        self.state = state.lower()

    def is_available(self) -> bool:
        return self.state == "available"

    def __eq__(self, other):
        return isinstance(other, Availability) and self.state == other.state

    def __str__(self):
        return self.state