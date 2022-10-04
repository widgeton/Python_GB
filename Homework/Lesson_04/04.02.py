# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# in 54             in 9990                     in 650
# out [2, 3, 3, 3]  out [2, 3, 3, 3, 5, 37]     out [2, 5, 5, 13]

def is_prime_number(number: int):
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def prime_divisors(number: int) -> list:
    result = []
    num_range = number // 2 + 1
    k = 2
    while k <= num_range:
        if is_prime_number(k) and number % k == 0:
            result.append(k)
            number /= k
            k -= 1
        k += 1
    return result


num = int(input("Input natural number: "))
print(prime_divisors(num))
