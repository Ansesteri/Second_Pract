DAYS_IN_MONTH = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

def tommorow(day, month, year):
    """
    """
    day += 1
    if day > DAYS_IN_MONTH[month] \
            + leap_year(year) if month == 2 else 0:
        day = 1
        month += 1
    if month == 13:
        month = 1
        year += 1
    return day, month, year

def yesterday(day, month, year):
    """
    """
    day -= 1
    if day == 0:
        month -= 1
        if month == 0:
            month = 12
            year -= 1
        day = DAYS_IN_MONTH[month] \
            + leap_year(year) if month == 2 else 0
    return day, month, year

def leap_year(year):
    """
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

day, month, year = map(
    int,
    input('Enter date, example: 15.03.2020 -> ').split('.')
)
print(tommorow(day, month, year))
print(yesterday(day, month, year))
