from collections import Counter

def can_be_poly(str_to_check):
    c = Counter()
    for word in (x for x in str_to_check):
        c[word] += 1
    c = list(filter(lambda x: x % 2 == 1, c.values()))
    if len(c) < 2:
        return True
    else:
        return False



print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))
