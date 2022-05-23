def summ(number):
    summ_number = 0
    for i in number:
        summ_number += int(i)
    return summ_number

def quantity(number):
    quantity_number = 0
    for i in number:
        quantity_number += 1
    return quantity_number

number = input('Введите число: ')
summ = summ(number=number)
quantity = quantity(number=number)

print('Сумма чисел:', summ)
print('Количество цифр в числе:', quantity)
print('Разность суммы и количества цифр:', summ - quantity)