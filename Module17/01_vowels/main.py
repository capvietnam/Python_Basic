list_symbols = []

for i in input('Введите текст: '):
    if i in ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']:
        list_symbols.append(i)

print('Список гласных букв:', list_symbols)
print('Длина списка:', len(list_symbols))