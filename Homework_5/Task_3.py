# 3. Создайте программу для игры в ""Крестики-нолики"".


def print_fields(field):
    print(f"\t|   {field[0]:<4}|   {field[1]:<4}|   {field[2]:<4}|")
    print("\t|-----------------------|")
    print(f"\t|   {field[3]:<4}|   {field[4]:<4}|   {field[5]:<4}|")
    print("\t|-----------------------|")
    print(f"\t|   {field[6]:<4}|   {field[7]:<4}|   {field[8]:<4}|")
    print("\t|-----------------------|")


def move_player(player, str_, field):
    move = int(input(f"Ходит {player} игрок. Введите цифру поля: "))
    field[move-1] = str_


def win_case_x(list_, value):
    if ((list_[0]) == value and (list_[4]) == value and (list_[8]) == value):
        return -1
    elif ((list_[2]) == value and (list_[4]) == value and (list_[6]) == value):
        return -1


def win_case_ver(list_, value):
    for i in range(0, 4):
        if (list_[i] == value and list_[i + 3] == value and list_[i + 6] == value):
            return -1


def win_case_hor(list_, value):
    for j in range(0, 7, 3):
        if (list_[j] == value and list_[j + 1] == value and list_[j + 2] == value):
            return -1


def check_win_options(_list, player, value):
    if win_case_x(_list, value) == -1 or win_case_ver(_list, value) == -1 or win_case_hor(_list, value) == -1:
        print(f"Поздравляю! Игрок {player} победил!")
        return -1


field_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print_fields(field_list)

j = 0
while j < len(field_list):
    move_player("1", "X", field_list)
    print_fields(field_list)
    if j >= 2:
        if check_win_options(field_list, "1", "X") == -1:
            break
    move_player("2", "O", field_list)
    print_fields(field_list)
    if j >= 2:
        if check_win_options(field_list, "2", "O") == -1:
            break
    j += 1
