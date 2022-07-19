class Date:
    def __init__(self, day: str, month: str, year: str) -> None:
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def from_string(date: str):
        day, month, year = date.split('-')
        return Date(day, month, year)

    def get_date(self):
        return self.day, self.month, self.year

    @classmethod
    def is_date_valid(cls, date_unverified) -> bool:
        date_unverified = Date.from_string(date_unverified)
        day, month, year = date_unverified.get_date()
        return 0 <= int(day) <= 31 and 0 <= int(month) <= 12

    def __str__(self):
        return f'День: {self.day}\tМесяц: {self.month}\tГод: {self.year}'

date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))