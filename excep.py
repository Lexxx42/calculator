""" This file is for data validation. Coded by Alexander Konukhov. """


def validation_mode() -> int:
    """ Function for  check user input for calculator's mode. """
    while True:
        try:
            calc_mode = int(input("Enter the calculator's mode: "))
        except ValueError:
            print('Incorrect input! Input must be an integer')
            continue
        if calc_mode in [0, 1, 2]:
            return calc_mode
        print("Incorrect input! Please look at the available modes")
