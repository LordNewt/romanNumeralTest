import unittest
from src.romanConversion import RomanConversion

class RomanConversionTest(unittest.TestCase):
    def setUp(self):
        self.converter = RomanConversion()

    #
    # Basic digit tests
    #
    def test_one_to_numeral(self):
        self.assertEqual('I', self.converter.toRomanNumeral(1))

    def test_two_to_numeral(self):
        self.assertEqual('II', self.converter.toRomanNumeral(2))

    def test_five_to_numeral(self):
        self.assertEqual('V', self.converter.toRomanNumeral(5))

    def test_ten_to_numeral(self):
        self.assertEqual('X', self.converter.toRomanNumeral(10))

    def test_fifty_to_numeral(self):
        self.assertEqual('L', self.converter.toRomanNumeral(50))

    def test_one_hundred_to_numeral(self):
        self.assertEqual('C', self.converter.toRomanNumeral(100))

    def test_five_hundred_to_numeral(self):
        self.assertEqual('D', self.converter.toRomanNumeral(500))

    def test_one_thousand_to_numeral(self):
        self.assertEqual('M', self.converter.toRomanNumeral(1000))

    #
    # Multi-digit test
    #
    def test_max_digits_to_numeral(self):
        self.assertEqual('MDCLXVI', self.converter.toRomanNumeral(1666))

    #
    # "Minus 1" tests
    #
    def test_four_to_numeral(self):
        self.assertEqual('IV', self.converter.toRomanNumeral(4))

    def test_nine_to_numeral(self):
        self.assertEqual('IX', self.converter.toRomanNumeral(9))

    def test_forty_to_numeral(self):
        self.assertEqual('XL', self.converter.toRomanNumeral(40))

    def test_ninety_to_numeral(self):
        self.assertEqual('XC', self.converter.toRomanNumeral(90))

    def test_four_hundred_to_numeral(self):
        self.assertEqual('CD', self.converter.toRomanNumeral(400))

    def test_nine_hundred_to_numeral(self):
        self.assertEqual('CM', self.converter.toRomanNumeral(900))

    #
    # Max multi-digit "minus" test
    #
    def test_max_minus_digits_to_numeral(self):
        self.assertEqual('CMXCIX', self.converter.toRomanNumeral(999))
