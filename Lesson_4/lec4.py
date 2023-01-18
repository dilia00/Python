# 1. Считать строку из набора чисел из файла. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел. Результат заисать в конец исходного файла (х1 х2).


# my_list = input("Введите числа через пробел: ").split(" ")
# print(max(my_list))
# print(min(my_list))


with open('test.txt', 'r') as k:
    data_list = list(map(int, k.read().split()))
    print(f'Максимальное число: {max(data_list)}\n'
          f'Минимальное число: {min(data_list)}')


# # 3. задайте два числа. Напишите программу, которая найдет НОК
# # (наименьшее общее кратное) этих двух чисел.

num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))

for i in range(1, num_1 * num_2 + 1):
    if i % num_1 == 0 and i % num_2 == 0:
        print(i)
        break


# def get_greatest_common_divisor(number_1: int, number_2: int) -> int:
#     while number_1 != 0 and number_2 != 0:
#         if number_1 > number_2:
#             number_1 = number_1 % number_2
#         elif number_1 < number_2:
#             number_2 = number_2 % number_1
#     return number_1 + number_2


# greatest_common_div = get_greatest_common_divisor(num_1, num_2)
# print(
#     f"НОК {num_1} и {num_2} = {round((num_1 * num_2)/greatest_common_div)}")


# # 2.Найдите корни квадратного уровнения Ax^2 + Bx +C =0 двумя способами
# # 1) с помощью мотематических формул нахождения корней квадратного уровнения
# # 2) с помощью дополнительных библиотек Python
# discr = (b^2) - (4 * a * c)
# x_1 = (-b + discr^(1/2)) / (2 * a)
# x_2 = (-b - discr^(1/2)) / (2 * a)
# Если discr < 0, то корней нет

def squre_def(A, B, C) -> tuple:
    D = B ** 2 - 4 * A * C
    print(f'Дискриминант= {D}')
    if D > 0:
        x1 = (-B + D ** 0.5) / (2 * A)
        x2 = (-B - D ** 0.5) / (2 * A)
        print(f'Корень x1= {x1}')
        print(f'Корень x2= {x2}')
        return x1, x2
    elif D == 0:
        x = -B / (2 * A)
        print(f'Корень x={x}')
        return x
    return 'Корней нет'


print(squre_def(1, 2, 1))
