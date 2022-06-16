list_symbol = list(i for i in input('Введите строку: '))
dict_symbol = dict()
for symbol in list_symbol:
    if symbol in dict_symbol.keys():
        dict_symbol[symbol] += 1
    else:
        dict_symbol[symbol] = 1

list_odd = list(number for number in dict_symbol.values() if number % 2 == 1)

if len(list_odd) <= 1:
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')