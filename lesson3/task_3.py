""" 3. Друкувати список list_ten = [10, 20, 30, 40, 50] реверсивно - тобто.
програма має повернути [50, 40, 30, 20, 10]."""

my_list = range(10, 51, 10)

print(tuple(my_list)[::-1])
# or

my_list = [*my_list]
my_list.reverse()
print(my_list)
