import datetime
import uuid
from logg import logging
import user_interface
import model_div
import model_mult
import model_pow
import model_sub
import model_sum
import compl


def session() -> tuple:
    session_id = uuid.uuid1()
    session_datetime = datetime.datetime.now()
    # logging.info('Create session: ',session_id)
    operation_result = start()
    # logging.info('Session params: ',operation_result)
    finish(operation_result[2])
    return session_id, session_datetime, operation_result


def start() -> tuple:
    user_interface.main_menu()
    number_type = user_interface.numb_type
    interface_data = user_interface.t
    number1 = interface_data[0]
    number2 = interface_data[1]
    operation = interface_data[2]
    match number_type:
        case 1:
            print('заданы вещественные числа')
            result = operations(number1, number2, operation)
        case 2:
            print('заданы комплексные числа')
            compl1 = compl.to_complex(number1)
            compl2 = compl.to_complex(number2)
            result = operations(compl1, compl2, operation)
        case _:
            print('числа не заданы, завершаем программу без вычислений')
            result = 'отсутствует'
    print(interface_data)  # для теста
    return number_type, interface_data, result


# работает с комплексными, если не указывать явно тип данных
def operations(a, b, o: int) -> str:
    match o:
        case 1:
            res = str(a + b)  # для теста
        case 2:
            res = str(a - b)  # для теста
        case 3:
            res = str(model_mult.mult(a, b))  # для теста
        case 4 | 41:
            res = str(model_div.div_universal_number(a, b))
        case 42:
            res = str(model_div.div_integer(a, b))
        case 43:
            res = str(model_div.div_modul(a, b))
        case 5 | 6:
            res = str(model_pow.pow_new(a, b))
        case _:
            res = 'error'
    return res


def finish(r: str) -> None:
    user_interface.view_result(r)
