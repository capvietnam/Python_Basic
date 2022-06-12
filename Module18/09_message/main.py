#
# list_text = list(i[::-1] if i.isalpha() else i[-2::-1] + i[-1] for i in input('Сообщение: ').split())
#
# print('Новое сообщение: ' + ' '.join(list_text))
dict_word = dict()
True_text = ''
isl_text = ''
text = input('Сообщение: ').split()
for i in text:
    if i[1:-2].isalpha() == False and True in list(k.isalpha() for k in i):
        for s in i:
            if s.isalpha() == False:
                t = i.split(s)
                True_text = t[0][::-1] + s + t[1][::-1]
                dict_word[i] = True_text

list_text = list(i[::-1] if i.isalpha()
                 else dict_word.setdefault(i) if i in dict_word.keys() else i[-2::-1] + i[-1] for i in text)

print('Новое сообщение: ' + ' '.join(list_text))