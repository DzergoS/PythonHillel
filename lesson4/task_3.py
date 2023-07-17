""" 3. Дано два цілих числа 'A' і 'В'.
Виведіть усі числа від `A` до `B` включно, в порядку зростання, якщо `A < B`,
або в порядку зменшення в іншому випадку."""

A = int(input('Введіть число A: '))
B = int(input('Введіть число B: '))

is_A_bigger_B = A > B

my_list = range(A, B - 1 if is_A_bigger_B else B + 1, -1 if is_A_bigger_B else 1)

print(*my_list)
