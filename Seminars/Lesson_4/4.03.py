# 3. Задайте два числа. Напишите программу, которая найдёт
#    НОК (наименьшее общее кратное) этих двух чисел.
from math import gcd

num_1 = int(input())
num_2 = int(input())

print(num_1 * num_2 // gcd(num_1, num_2))
