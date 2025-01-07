class PostalCode:
    def __init__(self, code):
        if not self._validate_postal_code(code):
            raise ValueError("Invalid postal code format.")
        self.code = code

    def _validate_postal_code(self, code):
        """
        Validates the postal code format.
        """
        return True

    def __eq__(self, other):
        return isinstance(other, PostalCode) and self.code == other.code

    def __str__(self):
        return self.code

