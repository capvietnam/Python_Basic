def unification(nice_list):
    for i in nice_list:
        if type(i) == int:
            new_list.append(i)
        else:
            unification(i)
    return new_list

def sum(*array1):
    summ = 0
    new_array = unification(array1)
    for i in new_array:
        summ += i
    return summ


new_list = []
print(sum([[1, 2, [3]], [1], 3]))
print(sum(1, 2, 3, 4, 5))
