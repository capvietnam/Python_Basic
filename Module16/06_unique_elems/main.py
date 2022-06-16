first_list = []
second_list = []

for i in range(3):
    first_list.append(int(input(f'Введите {i+1}-е число для первого списка: ')))

for i in range(7):
    second_list.append(int(input(f'Введите {i+1}-е число для второго списка: ')))

print('Первый список:', first_list)
print('Второй список:', second_list)

first_list.extend(second_list)
print('Новый первый список с уникальными элементами:', list(set(first_list)))
