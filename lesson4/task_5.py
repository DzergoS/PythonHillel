"""
5. Дано рядок.

  a. Виведіть третій символ цього рядка.

  b. виведіть передостанній символ цього рядка.

  с. виведіть перші п'ять символів цього рядка.

  d. виведіть весь рядок, крім двох останніх символів.

  e. виведіть усі символи з парними індексами (вважаючи, що індексація починається з 0,

  тому символи виводяться починаючиз першого).

  f. виведіть усі символи з непарними індексами, тобто, починаючи з другого символу рядка.

  g. виведіть усі символи у зворотному порядку.

  h. виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього.

  i. виведіть довжину цього рядка."""


def get_elements_at_indexes(string, even=True):
    arr = []
    for index, symbol in enumerate(string):
        if even and index % 2 == 0:
            arr.append(symbol)
        elif not even and index % 2 != 0:
            arr.append(symbol)
    return arr


user_string = input('Введіть рядок: ')

print('Виведіть третій символ цього рядка.', user_string[2])
print('виведіть передостанній символ цього рядка.', user_string[len(user_string) - 2])
print("виведіть перші п'ять символів цього рядка.", user_string[0:5])
print('виведіть весь рядок, крім двох останніх символів.', user_string[0:len(user_string) - 2])
print('виведіть усі символи з парними індексами', get_elements_at_indexes(user_string))
print('виведіть усі символи з непарними індексами, тобто, починаючи з другого символу рядка.',
      get_elements_at_indexes(user_string, even=False))
print('виведіть усі символи у зворотному порядку.', user_string.split().reverse())
print('виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього.',
      get_elements_at_indexes(user_string)[::-1] if len(user_string) % 2 != 0
      else get_elements_at_indexes(user_string, even=False)[::-1])
print('виведіть довжину цього рядка', len(user_string))
