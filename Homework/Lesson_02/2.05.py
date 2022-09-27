# Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
from random import randint

n = int(input("Number of elements: "))
A = []
for i in range(n):
    A.append(i)

print(A)

for i in range(len(A)):
    k = randint(0, len(A) - 1)
    temp = A[i]
    A[i] = A[k]
    A[k] = temp

print(A)
