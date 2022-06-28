import os


quantity_str = 0
quantity_word = 0
quantity_symbol = 0
min_symbol = None
dict_symbol = {}

speakers_file = open(os.path.abspath(os.path.join('..', '02_zen_of_python', 'zen.txt')), 'r', encoding='utf-8')

for element in speakers_file:
    quantity_str += 1
    for word in element.split():
        quantity_word += 1
        for symbol in word:
            quantity_symbol += 1
            if symbol.lower() in dict_symbol.keys():
                dict_symbol[symbol.lower()] += 1
            else:
                dict_symbol[symbol.lower()] = 0

speakers_file.close()

for key, value in dict_symbol.items():
    if value == min(dict_symbol.values()):
        min_symbol = key

print('Количество букв в файле:', quantity_symbol)
print('Количество слов в файле:', quantity_word)
print('Количество строк в файле:', quantity_str)
print('Наиболее редкая буква:', min_symbol)