def sum(*array1):
    summ = 0
    array = [ar for ar in array1]
    new_array = array[:]
    ind = 0
    while True:
        try:
            while isinstance(new_array[ind], list):
                item = new_array.pop(ind)
                for inner_item in reversed(item):
                    new_array.insert(ind, inner_item)
            ind += 1
        except IndexError:
            break
    for i in new_array:
        summ += i
    return summ



print(sum([[1, 2, [3]], [1], 3]))
print(sum(1, 2, 3, 4, 5))
