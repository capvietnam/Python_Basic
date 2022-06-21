last1 = 1
last2 = 1
number = 2
num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
while True:
    last1, last2 = last2, last1 + last2
    number += 1
    if number == num_pos:
        print('Число', last2)




