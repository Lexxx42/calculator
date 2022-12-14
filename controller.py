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


def session()-> tuple :
    operation_result = start()
    session_id = uuid.uuid1()
    session_datetime = datetime.datetime.now()
    finish(operation_result[2])
    # тут должно быть какое-то логирование
    return session_id, session_datetime, operation_result


def start()-> tuple :
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
    print(interface_data) # для теста
    return number_type, interface_data, result


# работает с комплексными, если не указывать явно тип данных
def operations(a, b, o:int)-> str :   
    match o:
        case 1:
            res = str(a+b) # для теста
        case 2:
            res = str(a-b) # для теста
        case 3:
            res = str(a*b) # для теста
        case 41:
            res = str(a/b) # для теста
        case 42:
            res = str('coming soon div//')
        case 43:
            res = str('coming soon div %')
        case 5:
            res = str('coming soon pow')
        case 6:
            res = str('coming soon pow = 0.5 as sqrt')
        case _:
            res = 'error'   
    return res    

def finish(r:str)-> None:  
    user_interface.view_result(r)

