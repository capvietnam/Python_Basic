#
# list_text = list(i[::-1] if i.isalpha() else i[-2::-1] + i[-1] for i in input('Сообщение: ').split())
#
# print('Новое сообщение: ' + ' '.join(list_text))
True_text = ''
isl_text = ''
text = input('Сообщение: ').split()
for i in text:
    if i[1:-2].isalpha() == False:
        for s in i:
            if s.isalpha() == False:
                t = i.split(s)
                True_text = t[0][::-1] + s + t[1][::-1]
                isl_text = i

list_text = list(i[::-1] if i.isalpha()
                 else True_text if i == isl_text else i[-2::-1] + i[-1] for i in text)

print('Новое сообщение: ' + ' '.join(list_text))