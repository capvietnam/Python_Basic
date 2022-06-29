from random import randint


ex = ['Syntax Errors', 'Exceptions', ]
summ = 0
with open('out_file.txt', 'w') as out_file:
    try:
        while summ < 777:
            new_number = input('Введите число: ')
            if randint(0, 13) == 0:
                raise Exception
            out_file.write(new_number + '\n')
            summ += int(new_number)
    except Exception:
        print('Вас постигла неудача!')

