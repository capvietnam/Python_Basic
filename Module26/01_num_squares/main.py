
class Random_number:

    def __init__(self, N):
        self.__N = N
        self.__counter = 0

    def __next__(self):
        if self.__N > self.__counter:
            self.__counter += 1
            return pow(self.__counter, 2)
        else:
            raise StopIteration

    def __iter__(self):
        return self


random_number = Random_number(3)
for i in random_number:
    print(i)


