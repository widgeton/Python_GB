# Даны два файла, в каждом из которых находится запись многочленов.
# Задача - сформировать файл, содержащий сумму многочленов.
# in
# "poly.txt"
# "poly_2.txt"
#
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 + 2*x^2 + 2*x^1 + 2 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 + 3*x^3 - 4*x^2 - 2*x^1 - 4 = 0
# 4*x^2 - 4 + 3*x^6 - 4*x^5 - 4*x^4 - 4*x^3 + 3*x^2 - 2*x^1 - 0 = 0


with open("sum_equations.txt", "a", encoding="utf-8") as file:
    str_1 = open("poly.txt", "r", encoding="utf-8").readlines()
    str_2 = open("poly_2.txt", "r", encoding="utf-8").readlines()
    if len(str_1) != len(str_2):
        print("The contents of the files do not match!")
    else:
        for i in range(len(str_1)):
            s1 = str_1[i].replace(' = 0\n', '')
            s2 = str_2[i].replace(' = 0\n', '')
            file.write(f"{s1} + {s2} = 0\n")

