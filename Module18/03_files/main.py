filename = input('Название файла: ')
err = 0

for i in "@№$%^&*().":
    if filename.startswith(i):
        print("название начинается на один из специальных символов")
        err += 1
if filename.endswith('.txt') == False and filename.endswith('.docx') == False:
    print("неверное расширение файла. Ожидалось .txt или .docx")
    err += 1
if err == 0:
    print("Файл назван верно.")
