#  3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19


def get_fractional_part(list_):
    new_list = []
    i = 0
    while i < len(list_):
        new_element = list_[i] - int(list_[i])
        new_list.append(round(new_element, 2))
        i += 1
    return new_list


def get_index_max_element(list_):
    index_max_element = 0
    i = 1
    while i < len(list_):
        if (list_[i] > list_[index_max_element]):
            index_max_element = i
        i += 1
    return index_max_element


def get_index_min_element(list_):
    index_min_element = 0
    i = 1
    while i < len(list_):
        if (list_[i] < list_[index_min_element]):
            index_min_element = i
        i += 1
    return index_min_element


list_fractional_part = get_fractional_part([1.1, 1.2, 3.1, 10.01])
max_ = list_fractional_part[get_index_max_element(list_fractional_part)]
min_ = list_fractional_part[get_index_min_element(list_fractional_part)]
difference = max_ - min_

print(
    f"Разница между max и min значением дробной части элементов = {difference}")
