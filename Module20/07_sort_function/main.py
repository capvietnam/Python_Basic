def tpl_sort(sort):
    for i in sort:
        if type(i) != int:
            return sort
    return tuple(sorted(sort))

print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))