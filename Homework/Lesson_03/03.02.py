# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Примеры:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
from random import sample


def multiply_pairs(array: list):
    result = []
    for i in range(len(array) // 2):
        result.append(array[i] * array[-(i + 1)])
    if len(array) % 2 != 0:
        result.append(array[len(array) // 2])
    return result


arr1 = sample(range(1, 10), 5)
pairs1 = multiply_pairs(arr1)
print(arr1, pairs1, sep=" => ")

arr2 = sample(range(1, 10), 4)
pairs2 = multiply_pairs(arr2)
print(arr2, pairs2, sep=" => ")
