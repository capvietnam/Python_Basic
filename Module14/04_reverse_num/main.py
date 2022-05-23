def coup(list):
    number3 = ''
    for i in str(list[::-1]):
        number3 += i
    return number3


def work_in_parts(number):
    list = str(number).split('.')
    return float(coup(list=list[0]) + '.' + coup(list=list[1]))


number1 = work_in_parts(number=input('Введите первое число: '))
number2 = work_in_parts(number=input('Введите второе число: '))

print('Первое число наоборот: ', number1)
print('Второе число наоборот: ', number2)
print('Сумма: ', number1 + number2)
