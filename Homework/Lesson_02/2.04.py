# Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов,
# заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

ind_1 = int(input("Position one: ")) - 1
ind_2 = int(input("Position two: ")) - 1
n = int(input("Number of elements: "))

A = []
for i in range(-n, n + 1):
    A.append(i)
print(A)
print(A[ind_1] * A[ind_2])
