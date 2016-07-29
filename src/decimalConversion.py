class DecimalConversion():

    decimalValues = {
        'V': 5,
        'I': 1
    }

    def toDecimalValue(self, input):
        input = input.upper()
        return self.decimalValues[input] if input in self.decimalValues else -1