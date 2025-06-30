import random
"""
Мутация 2 рандомных клеток в одной рандомной строке
Мутация 2 рандомных клеток в одном рандомном столбце
Мутация 2 абсолютно рандомных клеток
"""
def row_mutation(entity: list) -> None:
    numbers = list(range(1, 9))
    x = random.choice(numbers)
    first_y = random.choice(numbers)
    numbers.remove(first_y)
    second_y = random.choice(numbers)

    sym = entity[x][first_y]
    entity[x][first_y] = entity[x][second_y]
    entity[x][second_y] = sym


def column_mutation(entity: list) -> None:
    numbers = list(range(1, 9))
    y = random.choice(numbers)
    first_x = random.choice(numbers)
    numbers.remove(first_x)
    second_x = random.choice(numbers)

    sym = entity[first_x][y]
    entity[first_x][y] = entity[second_x][y]
    entity[second_x][y] = sym

def random_mutation(entity: list) -> None:
    numbers = list(range(1, 9))
    first_x = random.choice(numbers)
    second_x = random.choice(numbers)

    first_y = random.choice(numbers)

    if first_x == second_x:
        second_y = random.choice(numbers)

    else:
        numbers.remove(first_y)
        second_y = random.choice(numbers)

    sym = entity[first_x][first_y]
    entity[first_x][first_y] = entity[second_x][second_y]
    entity[second_x][second_y] = sym

