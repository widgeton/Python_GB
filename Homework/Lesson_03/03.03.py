# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# in 88 out 1011000
# in 11 out 1011


def decimal_in_binary(num: int):
    binary = ""
    while num:
        binary = str(num % 2) + binary
        num //= 2
    return binary


print(decimal_in_binary(88))
print(decimal_in_binary(11))
