# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.

import random


def get_polynomial(k):
    x = ""
    while k >= 0:
        rnd = random.randint(0, 100)
        if k == 0 and ((rnd) == 1 or (rnd) == 0):
            len_x = len(x)
            x = f"{x[:len_x-3]} = 0"
        elif k == 1 and (rnd) == 1:
            x += f"x + "
        elif (rnd) == 1:
            x += f"x^{(k)} + "
        elif (rnd) == 0:
            x += ""
        elif k == 1:
            x += f"{rnd} * x + "
        elif k == 0:
            x += f"{rnd} = 0"
        else:
            x += f"{rnd} * x^{(k)} + "
        k -= 1
    return x


num = int(input("Введите натуральную степень k: "))
print(get_polynomial(num))

with open("polynomial_1.txt", "w") as f_data_1:
    f_data_1.write(get_polynomial(num))

with open("polynomial_2.txt", "w") as f_data_2:
    f_data_2.write(get_polynomial(num))
