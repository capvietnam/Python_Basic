string_list = input('Введите строку: ').split()

for i in string_list:
    string_list[string_list.index(i)] = i[0].upper() + i[1:]

print(' '.join(string_list))