import os
from collections.abc import Iterable
print(os.path.abspath('main.py'))

def gen_files_dir(path: str) -> Iterable[str]:
    local_line = 0
    for root, dirs, files in os.walk(path):
        for File in files:
            if File.endswith('.py'):
                try:
                    with open(File, 'r') as file:
                        local_line = 0
                        for line in file.readlines():
                            if  line != '\n' and not line.startswith('#'):
                                local_line += 1
                except FileNotFoundError:
                    print('файл уже открыт')
                yield local_line

i = gen_files_dir('C:\\Users\\zenak\\Desktop\\projects\\pythonProject\\Python_Basic')
all_line = 0
for local_line in i:
    all_line += local_line



print(all_line)



