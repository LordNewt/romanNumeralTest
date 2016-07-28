import unittest


class RomanConversionTest(unittest.TestCase):
    def setUp(self):
        self.converter = RomanConversion()

    def test_one_to_numeral(self):
        self.assertEqual("I", self.converter.toRomanNumeral(1))
