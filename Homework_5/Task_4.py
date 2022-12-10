# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


def compression(str_):
    my_list = list(str_)
    new_list = []
    count = 1
    i = 1
    while i < len(my_list):
        if my_list[i-1] == my_list[i]:
            count += 1
        else:
            new_list.append(count)
            new_list.append(my_list[i-1])
            count = 1
        i += 1
    new_list.append(count)
    new_list.append(my_list[i-1])
    return "".join(map(str, new_list))


def decompression(str_):
    my_list = list(str_)
    new_list = []
    i = 0
    while i < len(my_list):
        if i % 2 == 0:
            temp = int(my_list[i])
        else:
            new_list.append(my_list[i] * temp)
        i += 1

    return ("".join(map(str, new_list)))


my_str = "gggguuukkksssbbaaefff"

print(compression(my_str))
print(decompression(compression(my_str)))
