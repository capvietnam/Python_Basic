total_symbol = 0
number = 1

with open('people.txt', 'r', encoding='utf-8') as people:
    for line in people.readlines():
        len_lines = len(line) -1
        try:
            if len(line)-1 < 4:
                raise BaseException
        except BaseException:
            print(f'менее трёх символов в строке {number}.')
        total_symbol += len(line)-1
        number += 1

print(total_symbol)
