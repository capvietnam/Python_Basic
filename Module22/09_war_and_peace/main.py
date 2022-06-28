import zipfile


dict_symbol = {}
archive = zipfile.ZipFile('voyna-i-mir.zip', 'r')
text = open('voyna-i-mir.txt', 'r', encoding='utf-8').read()

for str in text:
    for symbol in str:
        if symbol.isalpha():
            if symbol in dict_symbol.keys():
                dict_symbol[symbol] += 1
            else:
                dict_symbol[symbol] = 1

sorted_tuples = sorted(dict_symbol.items(), key=lambda item: item[1])
print(sorted_tuples[::-1])