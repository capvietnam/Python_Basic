nice_list = [1, 2, 3, 4, [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

new_list = []

def unification(nice_list):
    for i in nice_list:
        if type(i) == int:
            new_list.append(i)
        else:
            unification(i)
    return new_list

print(unification(nice_list=nice_list))