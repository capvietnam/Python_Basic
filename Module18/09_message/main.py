
list_letters1 = list(chr(i) for i in range(1072, 1103))
list_letters2 = list(chr(i) for i in range(1040, 1072))
list_letters = input('Сообщение: ').split(' ')
text2 = ''
for word in list_letters:
    list_letters3 = [i for i in word]
    text_shift = ''.join(list(list_letters3[(list_letters3.index(i) - len(word) + 1) % len(word)]
                              if i in list_letters3 else list_letters3[(list_letters3.index(i) - 1) % len(word)]
    if i in list_letters2 else i for i in word))
    text2.join(text_shift)
print("Новое сообщение:", text2)