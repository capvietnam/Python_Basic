summ = 0

speakers_file = open('numbers.txt', 'r')
for element in speakers_file:
    for sumbol in element:
        if sumbol.isdigit():
            summ += int(sumbol)

speakers_file.close()

answer_file = open('answer.txt', 'w')
answer_file.write(str(summ))
answer_file.close()
