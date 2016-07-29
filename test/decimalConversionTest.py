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