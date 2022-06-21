def slicer(check, symbol):
    new_list = list()
    quantity = 0
    for i in check:
        if i == symbol:
            quantity += 1
        if quantity == 1:
            new_list.append(i)
    if quantity > 1:
        new_list.append(symbol)
    return tuple(new_list)


print(slicer((), 2))