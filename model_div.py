# Вычисление комплексных чисел

# a = float(input("Введите действительную часть числа a: "))
# b = float(input(" Введите мнимую часть числа b: "))
# c = float(input("Введите действительную часть числа c: "))
# d = float(input(" Введите мнимую часть числа d: "))


def div_complex_number(delimoe: complex, delitel: complex):
    rez = delimoe / delitel
    return rez


# delimoe = complex(a, b) для теста
# delitel = complex(c, d) для теста

# rez = div_complex_number(delimoe, delitel) для теста


# Вычисление рациональных чисел

# delimoe = float(input("Введите делимое m: "))
# delitel = float(input("Введите делитель n: "))


def div_rational_number(delimoe: float, delitel: float):
    # if delitel == 0:
    #    print("Ошибка, на ноль делить нельзя") для теста
    #    return 0

    # else:
    return delimoe / delitel

# rez = div_rational_number(delimoe, delitel) для теста

# missing options: //, % for real numbers
