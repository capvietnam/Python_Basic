def new_zip(*args):
    min_len = min(len(t) for t in args)
    tpl_list = (tuple(struct[i] for struct in map(list, args)) for i in range(min_len))
    return tpl_list

# print(tuple(new_zip([{'x': 4}, 'b', 'z', 'd'], (10, {20,}, [30], 'z'))))
# for t in new_zip([{'x': 4}, 'b', 'z', 'd'], (10, {20,}, [30], 'z')):
#     print(t)


# a = [1, 2, 3, 4, 5]
# b = {1: 's', 2: 'q', 3: 4}
# c = (1, 2, 3, 4, 5)
# print(tuple(new_zip(a, b, c)))
# for t in new_zip(a, b, c):
#     print(t)