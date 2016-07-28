class RomanConversion():

    # Set up a map with the numeric value of each roman numeral. Listed
    # in descending value order.
    numeralValues = {
        'V': 5,
        'I': 1
    }

    def toRomanNumeral(self, input):
        outputStr = ''

        # Add digits until the remaining value is reduced to zero
        while input > 0:

            # Iterate over the numerals
            for numeral,value in self.numeralValues.items():
                # Don't attempt to evaluate if already at zero
                if input > 0:
                    # If the remaining value is greater than the current
                    # numeral value, append that numeral to the output
                    # and reduce the remaining value
                    while input >= value:
                        outputStr += numeral
                        input -= value

        # Return the numeral string
        return outputStr