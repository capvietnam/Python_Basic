# def calculating_math_func(data):
    # result = 1
    # for index in range(1, data + 1):
    #     result *= index
    # result /= data ** 3
    # result = result ** 10
    # return result

answer = {}
def calculating_math_func(data):
    if data in answer.keys():
        return answer[data]
    result = 1
    for index in range(1, data + 1):
        result *= index
    result /= pow(data, 3)
    result = pow(result, 10)
    answer[data] = result
    print(answer)
    return result

while True:
    calculating_math_func(int(input('Введите число: ')))