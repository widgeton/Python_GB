# Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in 5
# out [5.16, 8.62, 6.57, 7.92, 9.22]
#     Min: 0.16, Max: 0.92. Difference: 0.76
from random import uniform


def get_float_list(size, least, highest):
    array = []
    for i in range(size):
        array.append(round(uniform(least, highest + 1), 2))
    return array


def frac_max_minus_min(array):
    roster = array.copy()  # скопировал список чтобы не изменять исходный
    for i in range(len(roster)):
        roster[i] = round(roster[i] % 1, 2)
    return round(max(roster) - min(roster), 2)


arr = get_float_list(5, 1, 10)
diff = frac_max_minus_min(arr)
print(arr, diff, sep=" -> ")
# В ЭТОМ ЯЗЫКЕ СРОЧНО НАДО ЧТО-ТО ДЕЛАТЬ С ХРАНЕНИЕМ ВЕЩЕСТВЕННЫХ ЧИСЕЛ!!! :)
