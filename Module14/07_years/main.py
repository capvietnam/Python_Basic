def base(year1, year2):
    print(f'Годы от {year1} до {year2} с тремя одинаковыми цифрами:')
    by_numbers = []
    quantity = 0
    for yaer in range(year1, year2 + 1):
        for i in str(yaer):
            by_numbers.append(i)
        for s in by_numbers:
            for t in by_numbers:
                if s == t:
                    quantity += 1
            if quantity == 3:
                print(yaer)
                break
            quantity = 0
        by_numbers = []


base(year1=int(input('Введите первый год: ')), year2=int(input('Введите второй год: ')))
