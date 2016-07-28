class RomanConversion():

    def toRomanNumeral(self, input):
        outputStr = ''
        while input > 0:
            outputStr += 'I'
            input -= 1
        return outputStr