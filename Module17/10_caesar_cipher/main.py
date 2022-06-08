text = input('Введите сообщение: ')

list_letters1 = [chr(i) for i in range(ord('а'), ord('ь'))] + ([chr(i) for i in range(ord('a'), ord('w'))])
list_letters1.extend([chr(i) for i in range(ord('А'), ord('Ь'))] + [chr(i) for i in range(ord('A'), ord('W'))])
list_letters2 = [chr(t) for t in range(ord('э'), ord('я'))] + [chr(t) for t in range(ord('x'), ord('y'))]
list_letters2.extend([chr(t) for t in range(ord('Э'), ord('Я'))] + [chr(t) for t in range(ord('X'), ord('Y'))])

print(''.join([chr(ord(s)+3) if s in list_letters1 else chr(ord('а')+list_letters2.index(s))
if s in list_letters2 else s for s in text]))
