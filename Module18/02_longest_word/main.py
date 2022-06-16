def get_max_len_word(string_list):
   return sorted(string_list, key=len)[-1]


string_list = input('Введите строку: ').split()
string_word = get_max_len_word(string_list=string_list)

print('Самое длинное слово:', string_word, '\nДлина этого слова:', len(string_word))

