text1 = input('Первая строка: ')
text2 = input('Вторая строка: ')
list_symbol = list(i for i in text1)

for shift in range(len(text1)):
    text_shift = ''.join(list(list_symbol[(list_symbol.index(i) + shift) % len(text1)] for i in text1))
    if text2 == text_shift:
        print(f'Первая строка получается из второй со сдвигом {shift}.')
        break
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')


