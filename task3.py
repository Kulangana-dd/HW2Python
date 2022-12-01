# 3) Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month = (input('Введите номер месяца от 1 до 12: \n'))

# Через list
seasons = ['Зима', 'Весна', 'Лето', 'Осень']

if month == '1' or month == '2' or month == '12':
    print(seasons[0])
elif month == '3' or month == '4' or month == '5':
    print(seasons[1])
elif month == '6' or month == '7' or month == '8':
    print(seasons[2])
elif month == '9' or month == '10' or month == '11':
    print(seasons[3])
else:
    print('Такого месяца не существует')

# Через dict
seasons_dict = {'Зима': ('1', '2', '12'),
                'Весна': ('3', '4', '5'),
                'Лето': ('6', '7', '8'),
                'Осень': ('9', '10', '11')}

for i in seasons_dict:
    if month in seasons_dict.get(i):
        print(i)
