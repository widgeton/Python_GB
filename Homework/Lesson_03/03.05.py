# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# in 8 out -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
# in 5 out 5 -3 2 -1 1 0 1 1 2 3 5

def neg_pos_fib(num):
    fib = [0]
    first, second = fib[0], 1
    for i in range(num):
        fib.append(second)
        if i % 2 == 0:
            fib.insert(0, second)
        else:
            fib.insert(0, -second)
        first, second = second, first + second
    return fib


n = int(input("Input number: "))
print(neg_pos_fib(n))
