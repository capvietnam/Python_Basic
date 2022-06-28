import os
from pprint import pprint

quantity = 0
total_size = 0
speakers_file2 = os.walk(os.path.abspath(os.path.join('..', '..', 'module14')))
speakers_file = list(speakers_file2)
print(speakers_file[0][0])
print('Количество подкаталогов:', len(speakers_file[0][1]))

for i in range(len(speakers_file)):
    quantity += len(speakers_file[i][2])


for dirpath, dirnames, filenames in os.walk(os.path.abspath(os.path.join('..', '..', 'module14'))):
    for f in filenames:
        fp = os.path.join(dirpath, f)
        total_size += os.path.getsize(fp)


print('Размер каталога (в Кб):', total_size / 1024 )