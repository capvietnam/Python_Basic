import random

list1 = [round(random.uniform(5, 10), 2) for i in range(20)]
list2 = [round(random.uniform(5, 10), 2) for t in range(20)]

print(list1)
print(list2)

print([list1[s] if list1[s] > list2[s] else list2[s] for s in range(20)])