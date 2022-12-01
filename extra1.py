# 1) Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

user_number = input('Введите число: ')
sum_digits = 0
for i in user_number:
    if i.isdigit():
        sum_digits += int(i)
print(f'Сумма цифр числа {user_number} равна {sum_digits}')
