from PostalCode import PostalCode
class Location:
    def __init__(self, postal_code, latitude, longitude):
        self.postal_code = PostalCode(postal_code)
        
        self.latitude = latitude
        
        self.longitude = longitude

    def validate_latitude(self,latitude):
        if not (-90 <= latitude <= 90 ):
            raise ValueError("Latitude must be between -90 and 90")
        
    def validate_longitude(self,longitude):
        if not (-180 <= longitude <= 180 ):
            raise ValueError("Latitude must be between -180 and 180")
        
    def __eq__(self, other):
        return (
            isinstance(other, Location) and
            self.postal_code == other.postal_code and
            self.latitude == other.latitude and
            self.longitude == other.longitude
        )

    def __str__(self):
        return f"{self.postal_code}, ({self.latitude}, {self.longitude})"
