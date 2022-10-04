# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена,
# записать в файл полученный многочлен не менее 3-х раз.
# in 9
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
from random import randint, choice


def get_string(num: int):
    line = ""
    signs = ['+ ', '- ']
    while num:
        occ = randint(0, 10)
        if occ:
            line += f'{occ}*x^{num} '
            line += choice(signs)
        num -= 1
    line += f"{randint(0, 10)} = 0\n"
    return line


number = int(input("Input number: "))
with open("equations.txt", "a", encoding="utf-8") as file:
    if number > 0:
        file.write(get_string(number))
