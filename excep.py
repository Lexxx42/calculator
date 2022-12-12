""" This file is for data validation. Developed by Alexander Konukhov. """


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
        elif operation_type in range(5) and data_type == 2:
            return operation_type
        print("Incorrect input! Please look at the available operation codes.")


def validation_rational_input(main_operation) -> tuple[float, float]:
    """ Function for check user's input for rational numbers. """
    output_numbers = []
    while len(output_numbers) < 2:
        try:
            number = float(input(f"Enter number{len(output_numbers) + 1}: "))
        except ValueError:
            print('Incorrect input! Input must be a real number')
            continue
        if main_operation == 4 and len(output_numbers) == 1 and number == 0:
            print("Division by zero!")
            continue
        output_numbers.append(number)
    return output_numbers[0], output_numbers[1]


def validation_complex_input(main_operation) -> tuple[dict[float, float], dict[float, float]]:
    """ Function for check user's input for complex numbers. """
    output_complex = []
    number_input = 1
    while len(output_complex) < 4:
        try:
            if len(output_complex) % 2 == 0:
                number = float(input(f"Enter {number_input} real part: "))
            else:
                number = float(input(f"Enter {number_input} imaginary number: "))
                number_input += 1
        except ValueError:
            print('Incorrect input! Input must be a real number')
            continue
        if main_operation == 4 and len(output_complex) == 3 and output_complex[2] == 0 and number == 0:
            print("Division by zero!")
            continue
        output_complex.append(number)
    first_imaginary_number = {}
    second_imaginary_number = {}
    first_imaginary_number[output_complex[0]] = output_complex[1]
    second_imaginary_number[output_complex[2]] = output_complex[3]
    return first_imaginary_number, second_imaginary_number


def validation_additional_operation() -> int:
    """ Function for check user's input for additional operation. """
    while True:
        try:
            add_operation_code = int(input("Enter additional operation code: "))
        except ValueError:
            print('Incorrect input! Input must be an integer')
            continue
        if add_operation_code in range(4):
            return add_operation_code
        print("Incorrect input! Please look at the available additional operation codes.")
