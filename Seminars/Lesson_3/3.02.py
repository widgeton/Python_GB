# 2. Задайте список, состоящий из произвольных слов, количество задаёт пользователь.
#    Напишите программу, которая определит индекс второго вхождения строки в списке
#    либо сообщит, что её нет.
from random import choices


def get_word_list(size, word):
    array = []
    for i in range(size):
        elem = choices(word, k=3)
        array.append(''.join(elem))
    return array


def get_second_index(word, array):
    if array.count(word) > 1:
        ind1 = array.index(word)
        ind2 = array.index(word, ind1 + 1)
        print(ind2)
    else:
        print(-1)


arr = get_word_list(10, "xyz")
print(arr)
get_second_index("xyy", arr)
