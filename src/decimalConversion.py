class DecimalConversion():

    decimalValues = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

    def toDecimalValue(self, input):
        # Break the input into a character list that we can parse through
        input_list = list(input.upper())
        # Set the output value, the decimal value of the numerals, to zero
        total = 0
        # Set the initial "read" position in the character list to zero
        position = 0

        # Iterate over the numerals in the list until no more remain
        while position < len(input_list):
            # Check validity of the numeral
            if not input_list[position] in self.decimalValues:
                # Unknown letter - print it and return
                print('Invalid character: {0}'.format(input_list[position]))
                output = -1
                break
            # All valid, so add to output
            total += self.decimalValues[input_list[position]]

            # Always end an iteration by incrementing position
            position += 1

        # Return the total
        return total