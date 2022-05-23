# TODO здесь писать код

def smallest_divisor(number):
    for i in range(2, number + 1):
        if number % i == 0:
            print('Наименьший делитель, отличный от единицы:', i)
            break


number = smallest_divisor(number=int(input('Введите число: ')))
