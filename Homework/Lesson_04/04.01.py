# Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
#
# out
# 9.0000
from decimal import Decimal


num = Decimal(input('Enter a real number: '))
acc = Decimal(input("Enter the required accuracy '0.0001': "))

print(num.quantize(acc, "ROUND_HALF_UP"))
