text = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))
list_letters1 = [chr(i) for i in range(1072, 1103 - shift)]
list_letters2 = [chr(t) for t in range(1103 - shift, 1103)]

print(''.join([chr(ord(s)+shift) if s in list_letters1 else chr(ord('а')+list_letters2.index(s)-1)
if s in list_letters2 else s for s in text]))
