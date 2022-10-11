# Реализовать функцию, возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого)
# in 10 True
# out
# ['дом ночью мягкий', 'огонь завтра зеленый', 'лес вчера яркий',
#  'автомобиль сегодня веселый', 'город позавчера утопичный']
from random import choice


def jokes(lst_1, lst_2, lst_3, com):
    lst = []
    if len(com.split()) == 1 or com.split()[1] == 'False':
        for i in range(int(com.split()[0])):
            lst.append(f"{choice(lst_1)} {choice(lst_2)} {choice(lst_3)}")
    elif com.split()[1] == 'True':
        i = int(com.split()[0])
        while nouns and i:  # самый маленький массив
            a, b, c = choice(lst_1), choice(lst_2), choice(lst_3)
            lst.append("{} {} {}".format(a, b, c))
            lst_1.remove(a)
            lst_2.remove(b)
            lst_3.remove(c)
            i -= 1
    return lst


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

m = input("Enter command like '10 True' or '8 False': ")

print(jokes(nouns, adverbs, adjectives, m))
