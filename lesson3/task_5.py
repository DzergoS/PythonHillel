"""
5.  Користувач вводить число від 1 до 10,
    програма генерує рандомне число від 1 до 10,
    якщо числа співпадають надрукувати 'You won!' якщо ні - 'You lose!'.
    Дати користувачеві три спроби;)"""

import random

attempts = 3

while attempts:
    if int(input('Type 1 to 10 digit: ')) == random.randint(1, 10):
        print('You won!')
        break
    print('You lose!')
    attempts -= 1
