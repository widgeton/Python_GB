# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# 3 6
# 2 1
# 5.099

x1 = int(input("Enter x for first point: "))
y1 = int(input("Enter y for first point: "))

x2 = int(input("Enter x for second point: "))
y2 = int(input("Enter y for second point: "))

result = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
print(f"{result:.3f}")
