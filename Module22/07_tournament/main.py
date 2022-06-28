import os

txt_file = open(os.path.abspath(os.path.join('first_tour.txt')), 'r')
txt_file2 = open(os.path.abspath(os.path.join('second_tour.txt')), 'w')
score = txt_file.read(2)
dict_answer = {}
number = 0

for str_file in txt_file.readlines()[1:]:
    list_file = str_file.split()
    if score < list_file[2]:
        list_file[0], list_file[1] = list_file[1][0] + '.', list_file[0]
        dict_answer[list_file[2]] = ' '.join(list_file) + '\n'

txt_file2.write(f'{len(dict_answer)}\n')
sorted_tuple = sorted(dict_answer.items(), key=lambda x: x[0])

for i in sorted_tuple[::-1]:
    number += 1
    txt_file2.write(f'{number}) '+ i[1])

txt_file.close()
txt_file2.close()