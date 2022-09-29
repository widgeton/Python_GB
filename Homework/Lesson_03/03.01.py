# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётных позициях.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import sample


def sum_elems_odd_pos(array: list):
    amount = 0
    for i in range(0, len(array), 2):
        amount += array[i]
    return amount


arr = sample(range(1, 10), 5)
print(arr, sum_elems_odd_pos(arr), sep=" -> ")
