import unittest
from src.stations.domain.value_objects.PostalCode import PostalCode
class TestPostalCode(unittest.TestCase):

    def test_valid_postal_code(self):
        # Valid codes within Berlin's postal range
        valid_codes = ['10115', '12345', '14199']
        for code in valid_codes:
            postal_code = PostalCode(code)
            self.assertEqual(postal_code.code, code)

    def test_invalid_postal_code_length(self):
        # Invalid codes with incorrect lengths (should be 5 digits)
        invalid_codes = ['1011', '123456', '141']
        for code in invalid_codes:
            with self.assertRaises(ValueError):
                PostalCode(code)

    def test_invalid_postal_code_non_numeric(self):
        # Invalid codes with non-numeric values
        invalid_codes = ['abcde', '12ab5', '1419a']
        for code in invalid_codes:
            with self.assertRaises(ValueError):
                PostalCode(code)

    def test_postal_code_out_of_range(self):
        # Invalid postal codes outside the Berlin postal code range
        invalid_codes = ['9999', '15000', '20000']
        for code in invalid_codes:
            with self.assertRaises(ValueError):
                PostalCode(code)

    def test_postal_code_equality(self):
        # Testing equality of postal code objects
        code1 = PostalCode('10115')
        code2 = PostalCode('10115')
        code3 = PostalCode('14199')
        self.assertTrue(code1 == code2)  # Should be equal
        self.assertFalse(code1 == code3)  # Should not be equal

    def test_postal_code_string_representation(self):
        # Testing string representation of postal code
        code = PostalCode('10115')
        self.assertEqual(str(code), '10115')

    def test_edge_case_lowest_postal_code(self):
        # Testing the lowest possible Berlin postal code
        postal_code = PostalCode('10115')
        self.assertEqual(postal_code.code, '10115')

    def test_edge_case_highest_postal_code(self):
        # Testing the highest possible Berlin postal code
        postal_code = PostalCode('14199')
        self.assertEqual(postal_code.code, '14199')



if __name__ == '__main__':
    unittest.main()
