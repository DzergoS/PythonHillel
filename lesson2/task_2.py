""" 2. Напишіть програму, яка зчитує ціле число та виводить текст,
 аналогічний наведеному у прикладі (Прогалини важливі!).
 Перший рядок містить наступне значення, а другий рядок містить попереднє значення введеного числа:

    Please enter an integer number: 1234
    Next number for number 1234 is 1235.
    Previous number for number 1234 is 1233."""

digit = input("Please enter an integer number: ")

if digit.isdigit():
    digit = int(digit)
    print(f"Next number for number {digit} is {digit + 1}.")
    print(f"Previous number for number {digit} is {digit - 1}.")
else:
    print("Entered value is not digit")
