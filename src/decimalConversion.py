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
        input = input.upper()
        return self.decimalValues[input] if input in self.decimalValues else -1