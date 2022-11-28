
# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

#     *Пример:*

#     - Для N = 5:
#         1, -3, 9, -27, 81
#         1, -3, 9, -27, 81
#         (-3)**0 (-3)**1 (-3)**2 (-3)**3 (-3)**4


n = int(input('Введите число n - '))
for x in range(n):
    resalt = (-3)**x
    print(resalt, end=' ')


# Моржовый оператор
while x := int(input('--> ')) < 0:
    print('Введи число больше нуля')

x = int(input('--> '))
while x < 0:
    print('Введи число больше нуля')
    x = int(input('--> '))


# 2. Для натурального n создать последовательность (3*n + 1).

#     *Пример:*
#     - Для n = 6: 4, 7, 10, 13, 16, 19
n = int(input('Введите число n - '))
for x in range(1, n+1):
    resalt = 3*x+1
    print(resalt, end=' ')


# 3. Напишите программу, в которой пользователь будет задавать
# две строки, а программа - определять количество вхождений одной строки в другой.
# 'Я люблю Python'
# 'лю'
# --> 2
text = 'Я люблю Python'

char = input('Введите значение поиска: ')
len_char = len(char)
i = 0
count = 0
while i < len(text)-1:
    if char.lower() == text[i:len_char+i].lower():
        count += 1
    i += 1
print(count)


# text = 'Я люблю Python люблю'
# searchText = input('Введите строку для подсчета вхождения: ')

# list = text.split(searchText)
# print(len(list)-1)


# my_string = 'Я люблю Python'
# s2 = input("Введите строку для проверки вхождения: ")
# number = 0
# for i in range(len(my_string) - len(s2)+1):
#     if my_string[i:i+len(s2)] == s2:
#         number += 1
# print(number)
