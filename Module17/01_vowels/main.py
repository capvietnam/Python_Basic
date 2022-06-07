# TODO здесь писать код

text = input('Введите текст: ')
list_symbols = []
vowels = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
for i in text:
    if i in vowels:
        list_symbols.append(i)

print('Список гласных букв:', list_symbols)
print('Длина списка:', len(list_symbols))