from src.romanConversion import RomanConversion

exit = False
romanConverter = RomanConversion()
while not exit:
    user_input = input("Enter the number to convert: ")
    if user_input == 'exit':
        exit = True
    else:
        print("Converted to {0}".format(romanConverter.toRomanNumeral(int(user_input))))
