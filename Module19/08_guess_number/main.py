from random import randint
max_number = int(input('Введите максимальное число: '))
hidden_number = randint(1, max_number+1)
probably_right = set(number for number in range(1, max_number+1))

while True:
    answer_nubmer = input('Нужное число есть среди вот этих чисел: ')
    if answer_nubmer.lower() == 'помогите!':
        print('Артём мог загадать следующие числа:', ' '.join([str(i) for i in probably_right]))
    else:
        answer_nubmer = set(int(number) for number in answer_nubmer.split())
        if hidden_number in answer_nubmer:
            probably_right.intersection_update(answer_nubmer)
            print('Ответ Артёма: Да')
        else:
            probably_right.difference_update(answer_nubmer)
            print('Ответ Артёма: Нет')

    if len(probably_right) == 1:
        print('Артём загадал следующее число:', list(probably_right)[0])
        break
