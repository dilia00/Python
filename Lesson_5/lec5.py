# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# 'Я люблю Джавуабв абви Питон'
# 'Я люблю Питон'


# search_element = "абв"


# def func_1(find_char):
#     str_ = "Я люблю Джавуабв абви Питон"
#     _list = str_.split
#     for el in _list:
#         for i in range(len(el)):
#             if find_char == str_[i]:
#                 new_list.append(i)
#     if len(new_list) <= 1:
#         return -1
#     return new_list[1]
# string = 'Я люблю Джавуабв абви Питон'
# s1 = 'абв'
# print(' '.join([i for i in string.split() if i.count(s1) == 0]))


# my_str = 'Я люблю Джавуабв абви Питон'
# lst = my_str.split(" ")
# my_list = [i for i in lst if "абв" not in i]
# print(*my_list)


my_str = 'Я люблю Джавуабв абви Питон'
print(' '.join(list(filter(lambda word: "абв" not in word, my_str.split(" ")))))

# 2. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 5 6 7 9


# with open(file_path, 'r') as f:
#     list_new = list(map(int, f.read().split()))
#     list_new = [
#         list_new[i]+1 for i in range(len(list_new)-1) if list_new[i+1]-1 != list_new[i-1+1]]
#     print(list_new)


# for i in range(1, len(list_)):
#     if list_[i] - 1 != list_[i - 1]:
#         print(list_[i-1] + 1)

# fileText = r'secondfile.txt'
# with open(fileText, 'r') as ourFile:
#     strlist = ourFile.read().split(' ')

# x = list(map(int, strlist))
# searchNum(x)


# 3. Дан список чисел. Создайте список, в который попадают числа,
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.

#     *Пример:*

#     [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7] и т.д.

# my_list = [1, 5, 2, 3, 4, 6, 1, 7]
# new_list = [my_list[0]]
# for i in range(1, len(my_list)):
#     if my_list[i] > new_list[-1]:
#         new_list.append(my_list[i])
# print(new_list)
