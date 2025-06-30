import random
"""
Мутация 2 рандомных клеток в одной рандомной строке
Мутация 2 рандомных клеток в одном рандомном столбце
Мутация 2 абсолютно рандомных клеток
"""


def random_mutation(entity: list, insert_list_indexes: list) -> None:
    numbers = list(range(0, 81))
    for item in insert_list_indexes:
        numbers.remove(item[0] * 9 + item[1])

    first_sum = random.choice(numbers)
    numbers.remove(first_sum)
    second_sum = random.choice(numbers)

    first_x = first_sum // 9
    first_y = first_sum % 9

    second_x = second_sum // 9
    second_y = second_sum % 9

    sym = entity[first_x][first_y]
    entity[first_x][first_y] = entity[second_x][second_y]
    entity[second_x][second_y] = sym

def mutation_among_bad_rows(entity: list, insert_list_indexes: list, bad_rows_columns_indexes: list, row_column_flag: bool) -> None:
    numbers = []
    if row_column_flag == True:
        for item in bad_rows_columns_indexes:
            numbers += list(range(item * 9, item * 9 + 9))

        for item in insert_list_indexes:
            if item[0] in bad_rows_columns_indexes:
                numbers.remove(item[0] * 9 + item[1])
    else:
        for item in bad_rows_columns_indexes:
            numbers += list(range(item, 81, 9))

        for item in insert_list_indexes:
            if item[1] in bad_rows_columns_indexes:
                numbers.remove(item[0] * 9 + item[1])

    first_sum = random.choice(numbers)
    numbers.remove(first_sum)
    second_sum = random.choice(numbers)

    first_x = first_sum // 9
    first_y = first_sum % 9

    second_x = second_sum // 9
    second_y = second_sum % 9

    sym = entity[first_x][first_y]
    entity[first_x][first_y] = entity[second_x][second_y]
    entity[second_x][second_y] = sym




