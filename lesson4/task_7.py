"""** Дано два списки чисел. Надрукувати:

  - числа, що містяться одночасно як у першому списку, так і в другому

  - числа, що містяться в першому, але відсутні в другому

  - тільки унікальні для першого та другого списків"""


import random

random_list1 = random.choices(range(1, 100), k=10)
random_list2 = random.choices(range(1, 100), k=10)

print('Перший рандомний список\n', *random_list1)
print('Другий рандомний список\n', *random_list2, end='\n\n')

has_copies_arr = []
unique_first_arr = []
uniques_values_arr = set(random_list1) | set(random_list2)

for i in random_list1:
    has_copies = False
    for e in random_list2:
        if i == e:
            has_copies = True
            break
    if has_copies:
        has_copies_arr.append(i)
    if not has_copies:
        unique_first_arr.append(i)

print('Числа, що містяться одночасно як у першому списку, так і в другому\n', *has_copies_arr)
print('Числа, що містяться в першому, але відсутні в другому\n', *unique_first_arr)
print('Тільки унікальні для першого та другого списків\n', *uniques_values_arr)
