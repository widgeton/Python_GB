# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# В тексте используется разделитель пробел.
from random import sample


def get_txt(size: int, string: str):
    return ' '.join([''.join(sample(string, len(string))) for i in range(size)])


def del_substring(string: str, substring):
    return ' '.join(string.replace(substring, "").split())


# test_txt = "авб абв бав абв вба бав вба абв абв абв"
# print(test_txt, del_substring(test_txt, "абв"), sep="\n")

line = input("Input string like 'абв': ")
extent = int(input("Input list size: "))
txt = get_txt(extent, line)
if extent < 1:
    print("The size is incorrect")
else:
    print(txt, del_substring(txt, line), sep="\n")
