# 2) Для списка реализовать обмен значений соседних элементов,
# т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

number_of_elements = int(input('Введите количество элементов списка: '))
new_list = []
i = 0
el = 0
while i < number_of_elements:
    new_list.append(input(f'Введите {i+1} элемент: '))
    i += 1
print(f'Изначальный список:\n{new_list}')

for j in range(int(len(new_list) / 2)):
    new_list[el], new_list[el + 1] = new_list[el + 1], new_list[el]
    el += 2
print(f'Обмен значений соседних элементов:\n{new_list}')
