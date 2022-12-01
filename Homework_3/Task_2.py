# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def multiplication_paired_numbers(my_list):
    lenght_old_list = len(my_list)
    lenght_new_list = 0
    if (lenght_old_list % 2 == 0):
        lenght_new_list = lenght_old_list // 2
    else:
        lenght_new_list = (lenght_old_list // 2) + 1

    new_list = []
    i = 0
    while i < lenght_new_list:
        new_element = my_list[i] * my_list[lenght_old_list - 1 - i]
        new_list.append(new_element)
        i += 1
    return new_list


print(multiplication_paired_numbers([2, 3, 5, 6]))
