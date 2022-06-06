number = int(input('Кол-во чисел: '))
list_number = []

for i in range(number):
    list_number.append(int(input('Число: ')))

counter = 0
while list_number != list_number[::-1]:
    list_number.append(list_number[counter])
    counter += 1

print('Нужно приписать чисел:', counter)
print('Сами числа:', list_number[:counter][::-1])