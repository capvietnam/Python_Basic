def slicer(check, symbol):
    list_check = list(check)
    list_ansver = list()
    for i in check:
        if i == symbol:
            list_ansver.append(i)
            for t in list_check[1:]:
                list_ansver.append(t)
                if list_ansver[-1] == symbol:
                    return tuple(list_ansver)
        list_check.remove(i)



print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))