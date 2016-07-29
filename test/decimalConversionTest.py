import unittest
from src.decimalConversion import DecimalConversion

class DecimalConversionTest(unittest.TestCase):
    def setUp(self):
        self.converter = DecimalConversion()

    #
    # Basic digit tests
    #
    def test_i_to_number(self):
        self.assertEqual(1, self.converter.toDecimalValue('I'))

    def test_v_to_number(self):
        self.assertEqual(5, self.converter.toDecimalValue('V'))