# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#    Напишите программу, которая определит, присутствует ли в заданном списке число,
#    полученное от пользователя.
from random import sample


def find_num(num, q):
    q = q if q > 0 else -q
    arr = sample(range(1, q * 2), q)
    print(arr)
    if num in arr:
        return True
    return False


print(find_num(10, -10))
