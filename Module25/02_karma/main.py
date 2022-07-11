from random import randint, choice


class Buddhism:
    karma = 0

    def one_day(self):
        try:
            if randint(0, 10) == 0:
                exept = choice(['KillError', 'DrunkError', 'CarCrashError', 'GluttonyError', 'DepressionError'])
                raise BaseException(exept)
            else:
                self.karma += randint(1, 7)
        except BaseException:
            karma_file.write(exept + '\n')


buddhism = Buddhism()
with open('karma.log', 'w') as karma_file:
    while buddhism.karma <= 500:
        buddhism.one_day()