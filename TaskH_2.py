def yesterday(d, m, y):
    """Return date of previous day
    (day.month.year)

    Args:
        d (only from 1 to 31), m (only from 1 to 12), y (any positive number) (int)
    
    Returns:
        str: date of previous day
    """
    if 0 > d > 31:
        print("Please write the correct number")
    elif 0 > m > 12:
        print("Please write the correct number")