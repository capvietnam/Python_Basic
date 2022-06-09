def get_max_len_word(string_list):
   return sorted(string_list, key=len)[-1]


word_list = input('Введите строку: ').split()
max_word = get_max_len_word(string_list=word_list)

print('Самое длинное слово:', max_word, '\nДлина этого слова:', len(max_word))

