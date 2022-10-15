import writer as w
import converter as c
from os import path


def name_file():
    return input("Введите имя файла с расширением: ")


def write_in():
    f = input("Введите фамилию: ")
    n = input("Введите имя: ")
    o = input("Введите отчество: ")
    t = input("Введите номер телефона: ")
    d = input("Введите описание: ")
    return f, n, o, t, d


def turn():
    txt = """Введите
    для конвертации из txt в csv - 1
    для конвертации из csv в txt - 2"""
    print(txt)
    choice = input("Ввод: ")
    if choice == "1":
        name = name_file()
        if path.exists(name):
            c.txt_in_csv(name)
        else:
            print("Файла с таким именем нет")
    elif choice == "2":
        name = name_file()
        if path.exists(name):
            c.csv_in_txt(name)
        else:
            print("Файла с таким именем нет")
    else:
        print("Некорректный ввод")


def write_or_convert():
    txt = """Введите для записи в файл - 1
        для конвертации файла - 2"""
    print(txt)
    choice = input("Ввод: ")
    if choice == "1":
        w.w_in_txt(write_in(), name_file())
    elif choice == "2":
        turn()
    else:
        print("Некорректный ввод")
