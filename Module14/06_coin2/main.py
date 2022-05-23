def calculation_formula(x, y, r):
    if r > x and r > y:
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')


calculation_formula(x=float(input('X: ')), y=float(input('Y: ')), r=float(input('Введите радиус: ')))