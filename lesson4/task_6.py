"""6. * Даний список чисел.
Визначте, скільки в цьому списку елементів, які більше двох своїх сусідів (ліворуч і праворуч),
та виведіть кількість таких елементів.
Крайні елементи списку ніколи не враховуються, оскільки вони мають недостатньо сусідів.
"""


def get_value():
    input_value = int(input('Введіть число не менше за нуль: '))
    while input_value < 0:
        print('На жаль - воно менше нуля')
        input_value = int(input('Введіть число не менше за нуль: '))

    return input_value


array = []
currentValue = get_value()
while currentValue != 0:
    array.append(currentValue)
    currentValue = get_value()
else:
    print('Введен нуль')

counter = 0
for index, value in enumerate(array):
    if index != 0 and index != len(array) - 1 and value > array[index - 1] and value > array[index + 1]:
        counter += 1

print(f'{counter} елементів в цьому списку, які більше двох своїх сусідів')
