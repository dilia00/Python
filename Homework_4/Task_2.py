# 2. Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.


num = int(input("Введите число: "))
list_simple_multiplier = []
divider = 2
while num != 1:
    res = num / divider
    if num % divider == 0:
        list_simple_multiplier.append(divider)
        num = res
    else:
        divider += 1


print(list_simple_multiplier)
