# Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
# in 10
# out [20, 21, 40, 42, 60, 63, 80, 84, 100]

num = int(input("Enter number: "))
lst = [i for i in range(1, num + 1) if not i % 20 or not i % 21]
print(lst)
