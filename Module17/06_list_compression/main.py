import random


list_number = [random.randint(0, 2) for _ in range(int(input('Количество чисел в списке: ')))]

print('Список до сжатия:', list_number)

list(list_number.remove(i) for i in list_number[:] if i == 0)
print('Список после сжатия:', list_number)