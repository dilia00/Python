# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 0,56 -> 11


import random
num = input('Введите вещественное число: ')
integer_part = int(num.split(".")[0])
fractional_part = int(num.split(".")[1])


def get_sum_digits(number):
    sum = 0
    while (number > 0):
        sum = sum + number % 10
        number = number // 10
    return sum


print(
    f"Сумма цифр числа {num} = {get_sum_digits(integer_part) + get_sum_digits(fractional_part)}")


# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input('Введите число: '))


def digit_multiplication(num):
    multiplic = 1
    list_multiplic = []
    i = 1
    while i <= num:
        multiplic = multiplic * i
        list_multiplic.append(multiplic)
        i += 1
    return list_multiplic


print(digit_multiplication(number))


# 3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06


n = int(input('Введите число n - '))
res = 0
for i in range(1, n+1):
    res = res + ((1+(1/i))**i)
else:
    print(f"Сумма чисел последовательности = {round(res, 2)}")


# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0


num = int(input("Введите число N: "))
str_indices = input("Введите индексы через пробел: ").split(" ")
int_indices = list(map(int, str_indices))

list = []
for i in range(-num, num+1):
    list.append(i)

multiplication = 1
for j in int_indices:
    multiplication = multiplication * list[j]

print(list)
print(f"Произведение элементов с индексами {int_indices} = {multiplication}")


# 5. Реализуйте алгоритм перемешивания списка.

list_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in list_:
    new_index = random.randint(0, 9)
    temp = list_[new_index]
    list_[new_index] = list_[i]
    list_[i] = temp
print(list_)
