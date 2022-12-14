a = float (input("Введите действительную часть числа a: "))
b = float (input(" Введите мнимую часть числа b: "))
c = float (input("Введите действительную часть числа c: "))
d = float (input(" Введите мнимую часть числа d: "))

def div_complex_number(delimoe: complex, delitel: complex):
    rez = delimoe / delitel
    return rez

delimoe = complex(a, b) 
delitel = complex(c, d) 

rez = div_complex_number(delimoe,delitel)  





