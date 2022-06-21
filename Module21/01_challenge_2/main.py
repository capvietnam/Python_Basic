num = 0
def print_number(number):
    global num
    if number == num:
        return number
    else:
        num += 1
        print(num)
        return print_number(number)


print_number(10)