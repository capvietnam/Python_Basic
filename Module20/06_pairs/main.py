from random import randint


list_number = list(randint(0, 10) for i in range(10))
list_answer = list()


for i in range(0, 10, 2):
    list_answer.append((list_number[i], list_number[i+1]))

print(list_answer)
print(list((list_number[t], list_number[t+1]) for t in range(0, 10, 2)))
