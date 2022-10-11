# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.
# in 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]
from random import randint

size = int(input("Enter size: "))
lst = [randint(1, 30) for _ in range(size)]
new_lst = [lst[i] for i in range(1, len(lst)) if lst[i] > lst[i - 1]]
print(lst, new_lst, sep="\n")
