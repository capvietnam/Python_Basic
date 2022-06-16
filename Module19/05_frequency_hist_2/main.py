
dict_symbol = dict()

for symbol in input('Введите текст: '):
    if symbol in dict_symbol:
        dict_symbol[symbol] += 1
    else:
        dict_symbol[symbol] = 1

print('Инвертированный словарь частот:')
for value in range(1, max(dict_symbol.values())+1):
    list_key = list()
    for key in dict_symbol.keys():
        if dict_symbol[key] == value:
            list_key.append(key)
    if list_key:
        print(value, ':', list_key)
