from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
import random
import sys

FIELD_SIZE = 9
POPULATION_SIZE = 200
P_CROSSOVER = 0.5
P_MUTATION = 0.5
MAX_GENERATIONS = 150


class Solution:
    def __init__(self, id=int, generation=int):
        self.id = id
        self.generation = generation
        self.field = [[0 for _ in range(FIELD_SIZE)] for _ in range(FIELD_SIZE)]

# def evaluate():
# def crossover():
# def grade():

test = [
    [6, 4, 3, 5, 9, 7, 8, 2, 1],
    [1, 2, 8, 6, 4, 3, 5, 7, 9],
    [7, 5, 9, 2, 1, 8, 4, 6, 3],
    [4, 6, 2, 7, 5, 1, 3, 9, 8],
    [9, 3, 1, 8, 6, 4, 2, 5, 7],
    [5, 8, 7, 3, 2, 9, 1, 4, 6],
    [3, 7, 5, 4, 8, 6, 9, 1, 3],
    [8, 9, 4, 1, 7, 2, 6, 3, 5],
    [2, 1, 6, 9, 3, 5, 7, 8, 4]
]


# ========================== fitness calculation
def fitness_full(individual):
    amount = 0
    for line in individual:
        amount += len(set(line))

    for column in zip(*individual):
        amount += len(set(column))

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = [individual[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            
            amount += len(set(square))

    return amount

def fitness_cut(individual):
    amount = 0
    for line in individual:
        if len(set(line)) == 9:
            amount += 1 

    for column in zip(*individual):
        if len(set(column)) == 9:
            amount += 1

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = [individual[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            
            if len(set(square)) == 9:
                amount += 1

    return amount
# ========================== fitness calculation


# ========================== selection
def group_tournament_selection(population, k=3):
    random.shuffle(population) 
    best_individuals = []
    
    for i in range(0, len(population), k):
        group = population[i:i + k]
        best_in_group = max(group, key=fitness_full)
        best_individuals.append(best_in_group)
    
    return best_individuals
# ========================== selection



def main():
    print(FIELD_SIZE)
    print(POPULATION_SIZE)
    print(P_CROSSOVER)
    print(P_MUTATION)
    print(MAX_GENERATIONS)


if __name__ == "__main__":
    print(fitness_full(test))