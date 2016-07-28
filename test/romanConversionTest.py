import unittest
from src.romanConversion import RomanConversion

class RomanConversionTest(unittest.TestCase):
    def setUp(self):
        self.converter = RomanConversion()

    def test_one_to_numeral(self):
        self.assertEqual("I", self.converter.toRomanNumeral(1))

    def test_two_to_numeral(self):
        self.assertEqual("II", self.converter.toRomanNumeral(2))
