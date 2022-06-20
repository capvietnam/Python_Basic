from collections import Counter

def slicer(check, symbol):
    new_list = list()
    qyantity = 0
    for i in check:
        if i == symbol:
            qyantity += 1
        if qyantity == 1:
            new_list.append(i)
    if qyantity > 1:
        new_list.append(symbol)
    return tuple(new_list)


print(slicer((), 2))