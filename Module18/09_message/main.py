
dict_word = dict()
True_text = ''
isl_text = ''
text = input('Сообщение: ').split()


""""Ищем где внутри слов есть символы (отличные от букв) и переворачиваем относительно символа"""

for i in text:
    if i[0:-2].isalpha() == False and True in list(k.isalpha() for k in i):
        for s in i:
            if s.isalpha() == False:
                t = i.split(s)
                True_text = t[0][::-1] + s + t[1][::-1]
                dict_word[i] = True_text



""""Создаем список со значениями и переворачиваем без учета символа"""
list_text = list(f[::-1] if f.isalpha()
                 else dict_word.setdefault(f) if f in dict_word.keys() else f[-2::-1] + f[-1] for f in text)

print('Новое сообщение: ' + ' '.join(list_text))