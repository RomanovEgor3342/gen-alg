import random

def uniform_crossover_row(self, parent1: list[list[int]], parent2:list[list[int]]) -> list[list[int]]:
    child = [row.copy() for row in parent1]
    for row in range(9):
        if random.random() < 0.5:
            for column in range(9):
                child[row][column] = parent1[row][column]
        else:
            for column in range(9):
                child[row][column] = parent2[row][column]

    return child


def uniform_crossover_column(self, parent1: list[list[int]], parent2: list[list[int]]) -> list[list[int]]:
    child = [row.copy() for row in parent1]
    for column in range(9):
        if random.random() < 0.5:
            for row in range(9):
                child[row][column] = parent1[row][column]
        else:
            for column in range(9):
                child[row][column] = parent2[row][column]

    return child