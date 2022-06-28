import os
from pprint import pprint


dict_sybol = {}
txt_file = open(os.path.abspath(os.path.join('first_tour.txt')), 'r')
txt_file2 = open(os.path.abspath(os.path.join('second_tour.txt')), 'w')
text = txt_file.readline()
fraction = 1/len(list(i for i in text if i.isalpha()))

for symbol in text:
    if symbol.isalpha():
        if symbol.lower() in dict_sybol.keys():
            dict_sybol[symbol.lower()] += fraction
        else:
            dict_sybol[symbol.lower()] = fraction

dict_answer = dict(sorted(dict_sybol.items()))

for key, value in dict_answer.items():
    txt_file2.writelines(key + ' ' + str(value)[:5] + '\n')



