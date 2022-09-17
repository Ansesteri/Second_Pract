def lucky_num(a, b):
    """Return count of lucky tickets
    (even digits = odd digits)
    
    Args:
        - a, b (int): range limits
    
    Returns:
        - int: all numbers of lucky tickets from a to b
    """
    lucky_tickets = []
    for i in range(a, b+1):
        digits = 0
        number = i
        while number > 0:
            if number % 10 % 2 == 0:
                digits += 1
            number //= 10
        if 2 * digits == len(str(i)):
            lucky_tickets.append(i)
    return lucky_tickets

print(lucky_num(*list(map(int, input("Input range limit via space -->").split()))))