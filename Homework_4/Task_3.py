# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]


def find_count_el(list_, element):
    count = 0
    for k in range(len(list_)):
        if list_[k] == element:
            count += 1
    return count


my_list = [1, 1, 2, 3, 4, 4, 4]
new_list = []
for el in my_list:
    if find_count_el(my_list, el) == 1:
        new_list.append(el)

print(new_list)


# Второй способ решения - через втроенный метод

new_list_2 = []
for el in my_list:
    if my_list.count(el) == 1:
        new_list_2.append(el)

print(new_list_2)
