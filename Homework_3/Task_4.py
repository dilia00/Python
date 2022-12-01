# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input("Введите десятичное число: "))


def convert_number_to_binary(num):
    binary_num = 0
    count_ = 1
    while (num > 0):
        binary_num = binary_num + (num % 2) * count_
        count_ = count_ * 10
        num = num // 2
    return binary_num


bin_num = convert_number_to_binary(number)
print(f"{number} -> {bin_num}")


# Решение с помощью рекурсии


def dec_to_bin(num):
    if (num == 0):
        return
    else:
        dec_to_bin(num // 2)
        print((num % 2), end="")


dec_to_bin(number)
