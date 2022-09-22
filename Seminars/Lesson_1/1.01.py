max = int(input("Введите число: "))
for i in range(4):
    num = int(input("Введите число: "))
    if num > max:
        max = num
print("Число", max, "- максимальное")
