def Hofstadter(list_numbers: list):
    if list_numbers == [1, 2]: return
    list_numbers2 = list_numbers[:]
    while True:
        new_number = list_numbers2[-list_numbers2[-1]] + list_numbers2[-list_numbers2[-2]]
        if new_number > pow(10, 3): return
        list_numbers2.append(new_number)
        yield new_number


for number in Hofstadter([1, 1]):
    print(number)
