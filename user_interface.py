""" This file is for user interface. Coded by Alexander Konukhov. """
from excep import validation_mode


def main_menu() -> None:
    """ This function is for main menu of calculator. """
    print("""Calculator welcomes you!
    
    
Working with:
1 - rational
2 - complex
0 - exit
""")

    mode = validation_mode()
    choose_calculation(mode)


def choose_calculation(mode) -> None:
    return


main_menu()
