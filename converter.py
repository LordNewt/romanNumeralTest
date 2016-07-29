from src.romanConversion import RomanConversion
from src.decimalConversion import DecimalConversion

#
#   This script can be used to manually try out the decimal/numeral
#   conversion capabilities.
#
exit = False
romanConverter = RomanConversion()
decimalConverter = DecimalConversion()

# Keeps running until the user types 'exit'
while not exit:
    user_input = input("Enter the number to convert: ")
    if user_input == 'exit':
        exit = True
    else:
        # If the user input a decimal, convert to numeral. Otherwise, covert to a decimal
        if (user_input.isdigit()):
            print("Converted to {0}".format(romanConverter.toRomanNumeral(int(user_input))))
        else:
            print("Converted to {0}".format(decimalConverter.toDecimalValue(user_input)))
