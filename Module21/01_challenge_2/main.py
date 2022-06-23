def print_number(number, number1=1):
    if number == number1-1:
        return number
    print(number1)
    return print_number(number, number1+1)


print_number(10)