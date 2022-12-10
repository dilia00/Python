# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


import random


def lottery():
    num = int(input("Игрок выбери число 0 или 1: "))
    if num == random.randint(0, 1):
        print("Поздравляю! Ты делаешь первый ход!")
    else:
        print("Sorry! Первый ход делает другой игрок!")


def move_player(max_move, min_move):
    while True:
        number = int(input("Сколько конфет возмете?: "))
        if number > max_move or number < min_move:
            print(f"Возмите от {min_move} и не более чем {max_move} конфет")
        else:
            return number


def move_bot(max_move, min_move):
    num = random.randint(min_move, max_move)
    return num


def move_smart_bot(amount, max_move):
    num = amount % (max_move + 1)
    return num


def step_algorithm(name_player, amount, f_move):
    count_pl = f_move
    amount -= count_pl
    if amount <= 0:
        print(
            f"{name_player} взял {count_pl + amount} конфет, всего осталось: 0")
        print(f"Поздравляю! {name_player} выиграл!")
    else:
        print(f"{name_player} взял {count_pl} конфет, всего осталось: {amount}")
    return amount


#  Игра игрок против игрока
total = 2021
max_move_candies = 28
min_move_candies = 1


lottery()
while total > 0:
    total = step_algorithm("Игрок № 1", total, move_player(
        max_move_candies, min_move_candies))
    if total <= 0:
        break
    total = step_algorithm("Игрок № 2", total, move_player(
        max_move_candies, min_move_candies))


#  Игра игрок против глупого бота

while total > 0:
    total = step_algorithm("Игрок", total, move_player(
        max_move_candies, min_move_candies))
    if total <= 0:
        break
    total = step_algorithm("Бот", total, move_bot(
        max_move_candies, min_move_candies))


#  Игра игрок против умного бота

while total > 0:
    total = step_algorithm("Бот", total, move_smart_bot(
        total, max_move_candies))
    if total <= 0:
        break
    total = step_algorithm("Игрок", total, move_player(
        max_move_candies, min_move_candies))
