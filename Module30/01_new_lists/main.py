from typing import List
from functools import reduce

numbers2 = 1

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

floats2: List[float] = list(map(lambda x: round(pow(x, 3), 3), floats))
names2: List[str] = list(filter(lambda x: len(x) > 4, names))
numbers2: int = reduce((lambda x, y: x * y), numbers)

print(floats2)
print(names2)
print(numbers2)