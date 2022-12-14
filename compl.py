
def to_complex(number:dict)-> complex:
    for key, value in number.items():
        comple = complex(int(key), int(value))
    return comple

# def init(a,aj) -> complex:
#     a = int(a)
#     aj = int(aj)
#     new_a = complex(a,aj)
#     return new_a