""" This file is for data validation. Coded by Alexander Konukhov. """


def validation_mode() -> int:
    """ Function for check user's input for calculator's mode. """
    while True:
        try:
            calc_mode = int(input("Enter the calculator's mode: "))
        except ValueError:
            print('Incorrect input! Input must be an integer')
            continue
        if calc_mode in [0, 1, 2]:
            return calc_mode
        print("Incorrect input! Please look at the available modes.")


def validation_operation(data_type) -> int:
    """ Function for check user's input for operation. """
    while True:
        try:
            operation_type = int(input("Enter operation code: "))
        except ValueError:
            print('Incorrect input! Input must be an integer')
            continue
        if operation_type in range(7) and data_type == 1:
            return operation_type
        elif operation_type in range(6) and data_type == 2:
            return operation_type
        print("Incorrect input! Please look at the available operation codes.")


def validation_rational_input(main_operation) -> (int, int):
    """ Function for check user's input for rational numbers. """
    output_numbers = []
    while len(output_numbers) < 2:
        try:
            number = int(input(f"Enter number{len(output_numbers) + 1}: "))
        except ValueError:
            print('Incorrect input! Input must be an integer')
            continue
        if main_operation == 4 and len(output_numbers) == 1 and number == 0:
            print("Division by zero!")
            continue
        output_numbers.append(number)
        print(output_numbers)
        return output_numbers[0], output_numbers[1]
