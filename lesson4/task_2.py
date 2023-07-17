"""2. Програма запитує введення послідовності цілих невід'ємних чисел, доки не буде введено 0. Як тільки

буде введено 0 (нуль), програма повинна порахувати та вивести на екран:

- кількість введених чисел (завершальний 0 не рахується)

- їхню суму

- добуток

- середнє арифметичне (крім завершального числа 0)

- Визначити значення та порядковий номер найбільшого елемента послідовності. Якщо найбільших елементів є кілька,

виведіть порядковий номер першого з них. Нумерація елементів починається з 1 (однини)

- визначити кількість парних та непарних елементів у послідовності

- Визначити значення другого за величиною елемента в цій послідовності

- визначте, скільки елементів цієї послідовності дорівнюють її найбільшому елементу
"""
import math


def get_value():
    input_value = int(input('Введіть число не менше за нуль: '))
    while input_value < 0:
        print('На жаль - воно менше нуля')
        input_value = int(input('Введіть число не менше за нуль: '))

    return input_value


def get_odd_and_even_of_array(container):
    even_count = 0
    odd_count = 0
    for num in container:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count


def array_removed_value(container, value):
    array_copy = container.copy()
    while value in array_copy:
        array_copy.remove(value)
    return array_copy


array = []
currentValue = get_value()
while currentValue != 0:
    array.append(currentValue)
    currentValue = get_value()
else:
    print('Введен нуль')

array_sum = sum(array)
max_value = max(array)
even_odd_dict = get_odd_and_even_of_array(array)

print('кількість введених чисел: ', len(array))
print('їхня сума: ', array_sum)
print('добуток: ', math.prod(array))
print(f'Значення {max_value} під порядковий номером {array.index(max_value) + 1} є найбільшим елементом послідовності')
print(f'Значення другого за величиною елемента в цій послідовності: ', max(array_removed_value(array, max_value)))
print(f'{array.count(max_value)} елементів цієї послідовності дорівнюють її найбільшому елементу')
