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

def yesterday(d, m, y):
    """Return date of next day
    (day.month.year)

    Args:
        d (write day number), m (write month number), y (any positive number) (int)
    
    Returns:
        str: date of next day
    """
