"""4. По даному натуральному `n ≤ 9` виведіть драбинку з `n` сходинок,
`i`-я сходинка складається з чисел від 1 до `i` без прогалин.

  ````

  1

  12

  123

  1234

  12345

  ````"""

n = int(input("Введіть значення n (натуральне число ≤ 9): "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()