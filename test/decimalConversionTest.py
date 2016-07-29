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

    def test_x_to_number(self):
        self.assertEqual(10, self.converter.toDecimalValue('X'))

    def test_l_to_number(self):
        self.assertEqual(50, self.converter.toDecimalValue('L'))

    def test_c_to_number(self):
        self.assertEqual(100, self.converter.toDecimalValue('C'))

    def test_d_to_number(self):
        self.assertEqual(500, self.converter.toDecimalValue('D'))

    def test_m_to_number(self):
        self.assertEqual(1000, self.converter.toDecimalValue('M'))

    def test_invalid_returns_negative_one(self):
        self.assertEqual(-1, self.converter.toDecimalValue('R'))

    #
    # Multiple digit tests
    #
    def test_ii_to_number(self):
        self.assertEqual(2, self.converter.toDecimalValue('II'))

    def test_lots_of_numerals_to_number(self):
        self.assertEqual(2318, self.converter.toDecimalValue('MMCCCXVIII'))

    #
    # Reduction-numeral tests
    #
    def test_iv_to_number(self):
        self.assertEqual(4, self.converter.toDecimalValue('IV'))

    def test_ic_is_invalid(self):
        self.assertEqual(-1, self.converter.toDecimalValue('IC'))