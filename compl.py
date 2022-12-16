def to_complex(number: dict) -> complex:
    for key, value in number.items():
        comple = complex(int(key), int(value))
        # Почему тут инты? 0.8909 + i*0.8909 - не валидное комплексное число? - int(0.15) = 0. мы будем деление на ноль делать в обход эсепшенов!
    return comple

# def init(a,aj) -> complex:
#     a = int(a)
#     aj = int(aj)
#     new_a = complex(a,aj)
#     return new_a
