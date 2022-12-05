# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов
# (складываются числа, у которых "х" в одинаковых степенях).
import re


def get_poiy_dictionary(list_):
    list_values = []
    list_key = []
    for i in range(len(list_)):
        list_values.append(int(re.split(" * | = ", list_[i])[0]))
        list_key.append(re.split(" * | = ", list_[i])[-1])
    return dict(zip(list_key, list_values))


def sum_dictionary(list_):
    sum_dict = {}
    for dictionary in list_:
        for key in dictionary:
            try:
                sum_dict[key] += dictionary[key]
            except KeyError:
                sum_dict[key] = dictionary[key]
    return sum_dict


with open("polynomial_1.txt", "r") as k:
    data_list_1 = list(k.read().split(" + "))

with open("polynomial_2.txt", "r") as k:
    data_list_2 = list(k.read().split(" + "))

poiy_dict_1 = get_poiy_dictionary(data_list_1)
poiy_dict_2 = get_poiy_dictionary(data_list_2)

my_list = []
my_list.append(poiy_dict_1)
my_list.append(poiy_dict_2)

new_polynomial_dict = sum_dictionary(my_list)


new_poly = ""
for key, values in new_polynomial_dict.items():
    if (key == "0"):
        new_poly += f"{values} = {key}"
    else:
        new_poly += f"{values} * {key} + "

with open("sum_polynomial.txt", "w") as sum_data:
    sum_data.write(new_poly)
