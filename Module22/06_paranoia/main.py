import os


txt_file = open(os.path.abspath(os.path.join('text.txt')), 'r')
txt_file2 = open(os.path.abspath(os.path.join('cipher_text.txt')), 'w')
shift = 0

for message in txt_file:
    shift += 1
    alf = list(i for i in range(97, 123 - shift))
    alf2 = list(t for t in range(97, 98 + shift))
    new_message = list(chr(ord(symbol)+shift) if ord(symbol)+shift in alf else chr(ord(symbol)+shift)
                       for symbol in message if symbol.isalpha())
    new_message.append('\n')
    txt_file2.write(''.join(new_message))


txt_file2.close()
txt_file.close()

