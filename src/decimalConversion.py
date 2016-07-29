class DecimalConversion():

    decimalValues = {
        'M': { 'value': 1000, 'repeats': 3, 'reductor': 'C' },
        'D': { 'value': 500, 'repeats': 0, 'reductor': 'C' },
        'C': { 'value': 100, 'repeats': 3, 'reductor': 'X' },
        'L': { 'value': 50, 'repeats': 0, 'reductor': 'X' },
        'X': { 'value': 10, 'repeats': 3, 'reductor': 'I' },
        'V': { 'value': 5, 'repeats': 0, 'reductor': 'I' },
        'I': { 'value': 1, 'repeats': 3 }
    }

    def toDecimalValue(self, input):
        # Break the input into a character list that we can parse through
        input_list = list(input.upper())
        # Set the output value, the decimal value of the numerals, to zero
        total = 0
        # Set the initial "read" position in the character list to zero
        position = 0
        # A numeral can't be legal if it has more than 3 of the same character
        # in a row, so keep track of how many have been done
        repeats = 0
        last_numeral = ''

        # Iterate over the numerals in the list until no more remain
        while position < len(input_list):
            # Check validity of the numeral
            numeral = input_list[position]
            if not numeral in self.decimalValues:
                # Unknown letter - print it and return
                print('Invalid character: {0}'.format(numeral))
                return -1

            # Make sure the maximum iteration limit hasn't been exceeded
            if numeral == last_numeral:
                repeats += 1
                if repeats >= self.decimalValues[numeral]['repeats']:
                    print('Too many of {0} numeral in a row, invalid'.format(numeral))
                    return -1
            else:
                repeats = 0
            last_numeral = numeral

            # Next check if this is a "reduce by" numeral (like the I in IV)
            if position < len(input_list)-1:
                next_numeral = input_list[(position+1)]
                if self.decimalValues[numeral]['value'] < self.decimalValues[next_numeral]['value']:
                    # It IS a "reduce by" numeral. Check if it's a valid option
                    if numeral != self.decimalValues[next_numeral]['reductor']:
                        print('Invalid reductor numeral {0} for {1}'.format(numeral, next_numeral))
                        return -1
                    if repeats:
                        print('Illegal format, cannot repeat reduction digits')
                        return -1
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