"""6. Програма отримує на вхід число х.

  Даний список із 10 елементів [10, 20, 30, 40, 50, 60, 70, 80, 90, 100].

  Написати програму яка поверне:

  Чи є x серед елементів.


  Число на введення може бути як цілим числом, числом з точкою, що плаває, так і від'ємним,

  тобто. x = -10.00 має повернути що x є у списку.

  ** В ідеалі список повинен бути записаний як кортеж один раз."""

digit = float(input("Напиши x: "))

if abs(digit) in (10, 20, 30, 40, 50, 60, 70, 80, 90, 100):
    print("x є серед елементів")
else:
    print("x нема серед елементів")