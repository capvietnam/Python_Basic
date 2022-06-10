text2 = ''
text = input('Введите строку: ') + ' '
retr_symbol = text[0]
quantity = 0
for symbol in text:
    if retr_symbol != symbol:
        text2 += retr_symbol + str(quantity)
        retr_symbol = symbol
        quantity = 0
    quantity += 1
print('Закодированная строка:', text2)