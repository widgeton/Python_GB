# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# Добавьте игру против бота
# Подумайте, как наделить бота "интеллектом"
from random import choice

mode = int(input("Play with bot 1 - yes, 0 - no: "))

player_1 = input("Enter first player name: ")
player_2 = "Bot" if mode == 1 else input("Enter second player name: ")

p_move = player_1 if mode == 1 else choice([player_1, player_2])
candies = 174

while True:
    print(f"Remaining candies: {candies}")
    num = int(input(f"{p_move} move: "))
    if num < 1 or num > 28:
        print("You should take candies in range from 1 to 28!")
        continue
    candies -= num
    p_move = player_1 if p_move == player_2 else player_2
    if candies < 28:
        print(f"{p_move} - winner!")
        break

    if mode == 0:
        continue

    print(f"Remaining candies: {candies}")
    print(f"{p_move} move: {29 - num}")
    candies -= 29 - num
    p_move = player_1 if p_move == player_2 else player_2
    if candies < 28:
        print(f"{p_move} - winner!")
        break

# Рассчитать выигрышную стратегию (а значит наделить бота интеллектом) можно только:
# 1. если бот ходит всегда вторым (то есть если нет жеребьевки)
# 2. если количество всех конфет кратно максимальному числу конфет,
#    которые можно взять из кучи, плюс один (то есть 28 + 1 = 29, число 2021 не делится нацело на 29)
# При игре с ботом я включил эти условия.
