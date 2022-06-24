list_str = list()

speakers_file = open('zen.txt', 'r')
for element in speakers_file:
    list_str.append(element)
speakers_file.close()

for i in list_str[::-1]:
    print(i, end='')
