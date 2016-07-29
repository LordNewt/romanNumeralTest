class RomanConversion():

    # Set up a map with the numeric value of each roman numeral. Listed
    # in descending value order.
    numeralValues = {
        1000: { 'numeral': 'M'},
        500: { 'numeral': 'D'},
        100: { 'numeral': 'C'},
        50: { 'numeral': 'L'},
        10: { 'numeral': 'X' },
        5: { 'numeral': 'V', 'reductor': 1},
        1: { 'numeral': 'I'}
    }

    def toRomanNumeral(self, input):
        outputStr = ''

        # Add digits until the remaining value is reduced to zero
        while input > 0:

            # Iterate over the numerals. Python fights a little by not guaranteeing
            # order on a dictionary. However, I have made use of .sorted() to fix this
            for digit,info in sorted(self.numeralValues.items(), reverse=True):
                # Extract the roman numeral character, and the "minus" digit
                # for prepended numeral combinations
                numeral = info['numeral']
                reductor = info['reductor'] if 'reductor' in info else 0
                # Don't attempt to evaluate if already at zero
                if input > 0:
                    while input >= (digit - reductor):
                        # If the remaining value is greater than the current
                        # numeral value, append that numeral to the output
                        # and reduce the remaining value
                        if (input >= digit):
                            outputStr += numeral
                            input -= digit
                        # If the remaining value can be represented by two
                        # numerals with one being the "minus" numeral like
                        # 4 => IV, append that to the output and reduce the
                        # remaining value by difference in the numerals
                        else:
                            outputStr += self.numeralValues[reductor]['numeral'] + numeral
                            input -= (digit - reductor)


        # Return the numeral string
        return outputStr