# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
from itertools import groupby


def pack(path_reed, path_record):
    with open(path_reed, "r", encoding="utf-8") as file_r, \
            open(path_record, "a", encoding="utf-8") as file_a:
        lst = file_r.readlines()
        for i in lst:
            pack_str = ""
            count = 1
            for j in range(len(i) - 1):
                if i[j] == i[j + 1]:
                    count += 1
                else:
                    pack_str += f"{count}{i[j]}"
                    count = 1
            file_a.write(pack_str + "\n")


def unpack(path_reed, path_unpack):
    with open(path_reed, "r", encoding="utf-8") as file_r, \
            open(path_unpack, "a", encoding="utf-8") as file_a:
        lst = file_r.readlines()
        for i in lst:
            i = [''.join(g) for k, g in groupby(i.strip(), key=str.isdigit)]
            unpack_str = ''.join([int(i[j]) * i[j + 1] for j in range(0, len(i) - 1, 2)])
            file_a.write(unpack_str + "\n")


txt_file = "text_words.txt"
txt_arch = "text_code_words.txt"

pack(txt_file, txt_arch)
unpack(txt_arch, txt_arch)
