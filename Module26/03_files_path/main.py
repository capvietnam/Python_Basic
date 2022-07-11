import os
from collections.abc import Iterable


def find_dir(folder: str, path: str) -> Iterable[str]:
    print('Текущая директория', path)
    for i_elem in os.listdir(path):
        try:
            current_path = os.path.join(path, i_elem)
            if os.path.isdir(current_path) and i_elem != folder:
                yield from find_dir(folder, current_path)
            elif os.path.isfile(os.path.join(path, i_elem)):
                yield os.path.join(path, i_elem)
        except PermissionError:
            print('Нет разрешений')


user_folder = input('введите название каталога: ')
abs_path = os.path.abspath(os.path.join(os.path.sep))
result = find_dir(folder=user_folder, path=abs_path)
for i_path in result:
    print(i_path)