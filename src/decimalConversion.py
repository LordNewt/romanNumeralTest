class DecimalConversion():

    decimalValues = {
        'M': { 'value': 1000, 'reductor': 'C' },
        'D': { 'value': 500, 'reductor': 'C' },
        'C': { 'value': 100, 'reductor': 'X' },
        'L': { 'value': 50, 'reductor': 'X' },
        'X': { 'value': 10, 'reductor': 'I' },
        'V': { 'value': 5, 'reductor': 'I' },
        'I': { 'value': 1 }
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
                if self.decimalValues[numeral]['value'] < self.decimalValues[next_numeral]['value']:
                    # It IS a "reduce by" numeral. Check if it's a valid option
                    if numeral != self.decimalValues[next_numeral]['reductor']:
                        print('Invalid reductor numeral {0} for {1}'.format(numeral, next_numeral))
                        total = -1
                        break
                    total -= self.decimalValues[numeral]['value']
                    # Then move forward to the next numeral, since this one is done
                    position += 1
                    numeral = input_list[position]

            # Add the value of the numeral to the total
            total += self.decimalValues[numeral]['value']

            # Always end an iteration by incrementing position
            position += 1

        # Return the total
        return total