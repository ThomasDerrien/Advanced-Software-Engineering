class PostalCode:
    def __init__(self, code):
        if not self._validate_postal_code(code):
            raise ValueError(f"Invalid postal code format : {code} ")
        self.code = code

    def _validate_postal_code(self, code):
        """
        Validates the postal code format.
        Berlin postal codes are 5 digits long and range from 10115 to 14199.
        """

        if len(str(code)) != 5 :
            return False
        return 10115 <= int(code) <= 14199

    def __eq__(self, other):
        return isinstance(other, PostalCode) and self.code == other.code

    def __str__(self):
        return self.code
