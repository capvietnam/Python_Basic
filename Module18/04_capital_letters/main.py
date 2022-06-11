string_list = input('Введите строку: ').split()

for i in string_list:
    string_list[string_list.index(i)] = i.title()

print(' '.join(string_list))