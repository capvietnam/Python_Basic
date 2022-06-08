from random import randint
list_sticks = [i + 1 for i in range(int(input('Количество палок: ')))]
print(list_sticks)
throws = int(input('Количество бросков: '))
answer = ''

for throw in range(throws):
    numbers = randint(1, len(list_sticks) - 3)
    print(f'Бросок {throw + 1}. Сбиты палки с номера {numbers} по номер {numbers + 3}')
    numbers_list = list(range(numbers, numbers + 4))
    list_sticks = ['.' if t in numbers_list or t == '.' else t for t in list_sticks]

list_sticks = ['I' if s != '.' else '.' for s in list_sticks]

print('Результат: ' + ''.join(list_sticks))
