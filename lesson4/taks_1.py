"""Першого дня спортсмен пробіг `x` кілометрів, а потім він щодня збільшував пробіг на 10% від попереднього

значення. За цим числом `y` визначте номер дня, на який відстань спортсмена складе не менше `y` кілометрів.

Програма отримує на вхід числа `x` та `y` і має вивести одне число - номер дня"""

firstDayKm = float(input('Введіть километри за перший день: '))
endTrip = float(input('Введіть километри для рахування днів: '))

stepDay = 0.1

days = 1
total_distance = firstDayKm

while total_distance < endTrip:
    total_distance *= (1 + stepDay)
    days += 1

print(f'Щоб пробігти {int(endTrip)} км, потрібно: {days} днів')
