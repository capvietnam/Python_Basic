def Squares_numbers(max_number):
    for number in range(1, max_number + 1):
        yield pow(number, 2)


squares_numbers = Squares_numbers(3)
for i_number in squares_numbers:
    print(i_number)