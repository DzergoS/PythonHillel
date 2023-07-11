"""6. Шаховий кінь ходить буквою "Г" - на дві клітинки по вертикалі в будь-якому напрямку
і на одну клітинку по горизонталі, чи навпаки.
Дані дві різні клітини шахівниці, визначте, чи може кінь потрапити з першої клітини на другу одним ходом.
[Опціонально]
"""
import random

chess_map = {}

# Генеруємо координати для шахової дошки
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Заповнюємо словник координатами та значеннями
for letter in letters:
    for number in numbers:
        position = letter + str(number)
        chess_map[position] = (ord(letter) - ord('A') + 1, number)

# Друкуємо отриманий словник
print(chess_map)

random_place_1 = f'{letters[random.randint(0, 7)]}{numbers[random.randint(0, 7)]}'
random_place_2 = f'{letters[random.randint(0, 7)]}{numbers[random.randint(0, 7)]}'

coordinates_1 = chess_map[random_place_1]
coordinates_2 = chess_map[random_place_2]

success = 'Кінь може потрапити з першої клітини на другу одним ходом '
error = 'Кінь не може потрапити з першої клітини на другу одним ходом '

print('random_places', random_place_1, random_place_2)

if abs(coordinates_1[0] - coordinates_2[0]) == 2:
    if abs(coordinates_1[1] - coordinates_2[1]) == 1:
        print(success)
    else:
        print(error)
elif abs(coordinates_1[1] - coordinates_2[1]) == 2:
    if abs(coordinates_1[0] - coordinates_2[0]) == 1:
        print(success)
    else:
        print(error)
else:
    print(error)
