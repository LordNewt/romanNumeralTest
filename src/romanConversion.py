class RomanConversion():

    # Set up a map with the numeric value of each roman numeral. Listed
    # in descending value order.
    numeralValues = {
        1000: 'M"',
        500: 'D',
        100: 'C',
        50: 'L',
        10: 'X',
        5: 'V',
        1: 'I'
    }

    def toRomanNumeral(self, input):
        outputStr = ''

        # Add digits until the remaining value is reduced to zero
        while input > 0:

            # Iterate over the numerals. Python fights a little by not guaranteeing
            # order on a dictionary. However, I have made use of .sorted() to fix this
            for digit,numeral in sorted(self.numeralValues.items(), reverse=True):
                # Don't attempt to evaluate if already at zero
                if input > 0:
                    # If the remaining value is greater than the current
                    # numeral value, append that numeral to the output
                    # and reduce the remaining value
                    while input >= digit:
                        outputStr += numeral
                        input -= digit

        # Return the numeral string
        return outputStr