first_shirinka = list(range(160, 173, 2))
second_shirinka = list(range(162, 181, 3))

first_shirinka.extend(second_shirinka)
first_shirinka.sort()
print(first_shirinka)