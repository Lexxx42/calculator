import user_interface

def start():
    user_interface.main_menu
    a = user_interface.numb_type
    data = user_interface.t
    match a:
        case 1:
            print('заданы вещественные числа')
        case 2: 
            print('заданы комплексные числа')
        case _:
            print('числа не заданы, завершаем программу без вычислений')
    print(data)

    return(a)

    