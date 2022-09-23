# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input("Введите координату точки по оси x: "))
y = int(input("Введите координату точки по оси y: "))

if x > 0 and y > 0:
    print("Точка в первой четверти")
elif x < 0 and y > 0:
    print("Точка во второй четверти")
elif x < 0 and y < 0:
    print("Точка в третьей четверти")
elif x > 0 and y < 0:
    print("Точка в четвертой четверти")
else:
    print("Некорректные координаты")