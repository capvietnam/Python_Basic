# last1 = 1
# last2 = 1
# number = 2
# num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
# while True:
#     last1, last2 = last2, last1 + last2
#     number += 1
#     if number == num_pos:
#         print('Число', last2)


def fibo(number):
    if number in (1, 2):
        return 1
    return fibo(number-1) + fibo(number-2)

print(fibo(6))

