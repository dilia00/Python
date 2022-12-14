# 1. Для натурального n создать последовательность (3*n + 1).
#     *Пример:*
#     - Для n = 6: 4, 7, 10, 13, 16, 19

print("Задача 1:")
n = int(input('Введите число n - '))
print(list(3*i+1 for i in range(1, n+1)))

# for x in range(1, n+1):
#     resalt = 3*x+1
#     print(resalt, end=' ')


# 2. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06
print("Задача 2:")
n = int(input('Введите число n - '))
print(round(sum((1+(1/i))**i for i in range(1, n+1)), 2))

# res = 0
# for i in range(1, n+1):
#     res = res + ((1+(1/i))**i)
# else:
#     print(f"Сумма чисел последовательности = {round(res, 2)}")


# 3. Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной идексах.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12
print("Задача 3:")
list_ = [2, 3, 5, 9, 3]
print('Cумма = ', sum([list_[i] for i in range(len(list_)) if i % 2 != 0]))

# def sum_elements(my_list):
#     i = 1
#     my_sum = 0
#     while i < len(my_list):
#         my_sum += my_list[i]
#         i += 2
#     return my_sum

# print(sum_elements([2, 3, 5, 9, 3]))


# 4. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 0,56 -> 11
print("Задача 4:")
num = input('Введите вещественное число: ')
print(sum(map(int, filter(lambda el: "." not in el, list(num)))))

# integer_part = int(num.split(".")[0])
# fractional_part = int(num.split(".")[1])

# def get_sum_digits(number):
#     sum = 0
#     while (number > 0):
#         sum = sum + number % 10
#         number = number // 10
#     return sum

# print(
#     f"Сумма цифр числа {num} = {get_sum_digits(integer_part) + get_sum_digits(fractional_part)}")


# 5. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]
print("Задача 5:")
my_list = [1, 1, 2, 3, 4, 4, 4]
print(list(filter(lambda x: my_list.count(x) == 1, my_list)))

# new_list_2 = []
# for el in my_list:
#     if my_list.count(el) == 1:
#         new_list_2.append(el)

# print(new_list_2)
