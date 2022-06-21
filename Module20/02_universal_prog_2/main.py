def is_prime(id_symbol):
    for i in range(2, id_symbol):
        if id_symbol % i == 0:
            return False
    if id_symbol > 1:
        return True

def crypto(check):
    return list(symbol for id_symbol, symbol in enumerate(check) if is_prime(id_symbol=id_symbol))

print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto('О Дивный Новый мир!'))