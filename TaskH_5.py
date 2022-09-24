import random

def random_carriage(coupe_amount = 9):
    carriage = []
    coupe = {}
    for place in range(1, coupe_amount * 4 + 1):
        coupe[place] = random.choice([None, 'm', 'w'])
        if len(coupe) == 4:
            carriage.append(coupe)
            coupe = {}
    return carriage

print(random_carriage())
