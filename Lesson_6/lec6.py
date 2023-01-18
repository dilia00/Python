# 1. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
#     *Пример:*
#     2+2 => 4;
#     1+2*3 => 7;
#     1-2*3 => -5;
#     - Добавьте возможность использования скобок, меняющих приоритет операций.
#         *Пример:*
#         1+2*3 => 7;
#         (1+2)*3 => 9;


# string = '10+200*3'

# lst = []
# buf = ''
# for i in range(len(string)):
#     if string[i].isdigit():
#         buf += string[i]
#     else:
#         lst.append(int(buf))
#         lst.append(string[i])
#         buf = ''
# else:
#     lst.append(int(buf))
# print(lst)
# while ('*' in lst) or ('/' in lst):
#     mult = -1
#     if '*' in lst:
#         mult = lst.index('*')

#     div = -1
#     if '/' in lst:
#         div = lst.index('/')

#     if ((mult < div) and (mult != -1) and (div != -1)) or ((mult != -1) and (div == -1)):
#         res = lst[mult - 1] * lst[mult + 1]
#         lst = lst[:mult - 1] + [res] + lst[mult + 2:]
#     elif (div < mult) and (div != -1) and (mult != -1) or ((div != -1) and (mult == -1)):
#         res = lst[div - 1] / lst[div + 1]
#         lst = lst[:div - 1] + [res] + lst[div + 2:]
# while ('+' in lst) or ('-' in lst):
#     plus = -1
#     if '+' in lst:
#         plus = lst.index('+')

#     minus = -1
#     if '-' in lst:
#         minus = lst.index('-')

#     if ((plus < minus) and (plus != -1) and (minus != -1)) or ((plus != -1) and (minus == -1)):
#         res = lst[plus - 1] + lst[plus + 1]
#         lst = lst[:plus - 1] + [res] + lst[plus + 2:]
#     elif (minus < plus) and (minus != -1) and (plus != -1) or ((minus != -1) and (plus == -1)):
#         res = lst[minus - 1] - lst[minus + 1]
#         lst = lst[:minus - 1] + [res] + lst[minus + 2:]
# print(lst)


# def serch(lst):
#     for x in range(len(lst)):

#         if '*' or '/' in lst[x]:
#             resalt = int(lst[lst.index('*') - 1]) * int(lst[lst.index('*') + 1])
#                 lst.pop([lst.index('*') - 1])
#                 lst.pop([lst.index('*') + 1])
#                 lst[lst.index('*')] = resalt


#         if lst.index('*') > 0:
#         if lst.index('/') > 0:
#             if lst.index('*') < lst.index('/'):
#                 resalt = int(lst[lst.index('*') - 1]) * int(lst[lst.index('*') + 1])
#                 lst.pop([lst.index('*') - 1])
#                 lst.pop([lst.index('*') + 1])
#                 lst[lst.index('*')] = resalt
#             else:
#                 resalt = int(lst[lst.index('/') - 1]) / int(lst[lst.index('/') + 1])
#                 lst.pop([lst.index('/') - 1])
#                 lst.pop([lst.index('/') + 1])
#                 lst[lst.index('/')] = resalt
# else:
#             resalt = int(lst[lst.index('*') - 1]) * int(lst[lst.index('*') + 1])
#             lst.pop([lst.index('*') - 1])
#             lst.pop([lst.index('*') + 1])
#             lst[lst.index('*')] = resalt
#     elif lst.index('/') > 0:
#         resalt = int(lst[lst.index('/') - 1]) / int(lst[lst.index('/') + 1])
#         lst.pop([lst.index('/') - 1])
#         lst.pop([lst.index('/') + 1])
#         lst[lst.index('/')] = resalt


import re

s = '2+2*9/4-6'
match = re.findall(r'[+/*-]', s)
sort_a = sorted(match)
a = match
if '/' in sort_a:
    sort_a.remove('/')
    sort_a.insert(1, '/')

numbers = re.findall(r'\d', s)
list_of_numbers = list(map(int, numbers))
for _ in a:
    if _ == '*' or _ == '/':
        result = list_of_numbers[a.index(_) - 1]


for i in range(len(sort_a)):
    if sort_a[i] == '*':
        result *= int(s[s.index('*') + 1])
    elif sort_a[i] == '/':
        result /= int(s[s.index('/') + 1])
    elif sort_a[i] == '+':
        result += int(s[s.index('+') + 1])
    elif sort_a[i] == '-':
        result -= int(s[s.index('-') + 1])
print(result)
