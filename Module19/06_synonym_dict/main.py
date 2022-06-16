number = 1
dict_sin = dict()
for i in range(int(input('Введите количество пар слов: '))):
    new_pair = input('Первая пара: ').lower()
    list_sin = new_pair.split(' — ')
    dict_sin[list_sin[0]] = list_sin[1]
    dict_sin[list_sin[1]] = list_sin[0]

while True:
    word = input('Введите слово: ')
    if word in dict_sin.keys():
        print('Синоним:', dict_sin.get(word))
    else:
        print('Такого слова в словаре нет.')
