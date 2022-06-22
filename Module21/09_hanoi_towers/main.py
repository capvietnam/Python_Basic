# def move(n, start=1, finish=3):
#     if n == 1:
#         print(f"Переложить диск 1 со стержня номер {start} на стержень номер {finish}")
#     else:
#         move(n - 1, start, 6 - start - finish)
#         print(f"Переложить диск {n} со стержня номер {start} на стержень номер {finish}")
#         move(n - 1, 6 - start - finish, finish)

def move(n, start=1, finish=3):
     if n <= 0:
         return
     temp = 6 - start - finish
     move(n-1, finish=temp)
     print(f"Переложить диск {n} со стержня номер {start} на стержень номер {finish}")
     move(n-1, start=temp)

move(int(input("Введите кол-во дисков: ")))