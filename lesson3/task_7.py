"""7. Написати програму, яка знайде факторіал введеного користувачем числа.

Наприклад, факторіал числа 5 дорівнює добутку 1*2*3*4*5 = 120.

Формула знаходження факторіалу:

 n! = 1 * 2 * ... * n, де n - введене користувачем число."""

digit = int(input('введіть число для пошуку факторіала: '))

counter = 1
factorial = 1

while counter <= digit:
    factorial *= counter
    counter += 1

print('factorial', factorial)