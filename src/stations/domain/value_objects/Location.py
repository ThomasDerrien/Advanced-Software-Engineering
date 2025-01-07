from src.stations.domain.value_objects.PostalCode import PostalCode

class Location:
    def __init__(self, postal_code, latitude, longitude):
        # Validate and assign postal code
        self.postal_code = PostalCode(postal_code)

        # Validate latitude and longitude
        self.validate_latitude(latitude)
        self.validate_longitude(longitude)

        self.latitude = latitude
        self.longitude = longitude

    def validate_latitude(self, latitude):
        # Ensure latitude is between -90 and 90
        if not (-90 <= latitude <= 90):
            raise ValueError("Latitude must be between -90 and 90")

    def validate_longitude(self, longitude):
        # Ensure longitude is between -180 and 180
        if not (-180 <= longitude <= 180):
            raise ValueError("Longitude must be between -180 and 180")

    def __eq__(self, other):
        # Check for equality based on postal code, latitude, and longitude
        return (
            isinstance(other, Location) and
            self.postal_code == other.postal_code and
            self.latitude == other.latitude and
            self.longitude == other.longitude
        )

    def __str__(self):
        # Return string representation
        return f"{self.postal_code}, ({self.latitude:.2f}, {self.longitude:.3f})"
