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
            numeral = input_list[position]
            if not numeral in self.decimalValues:
                # Unknown letter - print it and return
                print('Invalid character: {0}'.format(numeral))
                total = -1
                break

            # Next check if this is a "reduce by" numeral (like the I in IV)
            if position < len(input_list)-1:
                next_numeral = input_list[(position+1)]
                if self.decimalValues[numeral] < self.decimalValues[next_numeral]:
                    # It IS a "reduce by" numeral, so reduce by that much instead
                    total -= self.decimalValues[numeral]
                    # Then move forward to the next numeral, since this one is done
                    position += 1
                    numeral = input_list[position]

            # Add the value of the numeral to the total
            total += self.decimalValues[numeral]

            # Always end an iteration by incrementing position
            position += 1

        # Return the total
        return total