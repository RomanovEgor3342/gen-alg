from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
import random
import sys
from sudoku_field import *
from mutation import *
import matplotlib.pyplot as plt

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


# ========================== print individual
def print_ind(ind):
    print('\n'.join([' '.join(list(map(str, ind[i]))) for i in range(9)]) + '\n')
# ========================== print individual

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
def group_tournament_selection(population, k=2):
    random.shuffle(population) 
    best_individuals = []
    
    for i in range(0, len(population), k):
        group = population[i:i + k]
        best_in_group = max(group, key=fitness_full)
        best_individuals.append(best_in_group)
    
    return best_individuals
# ========================== selection

# ========================== crossing
def one_point_crossing_sq(parent1, parent2, fixed_positions):
    child = [row.copy() for row in parent1] 

    num_squares_to_swap = random.randint(1, 7)

    all_squares = [(i, j) for i in range(0, 9, 3) for j in range(0, 9, 3)]
    
    squares_to_swap = random.sample(all_squares, num_squares_to_swap)
    
    for block_row, block_col in squares_to_swap:
        for i in range(block_row, block_row + 3):
            for j in range(block_col, block_col + 3):

                if (i, j) not in fixed_positions:
                    child[i][j] = parent2[i][j]
    
    return child

def uniform_crossover_sq(parent1, parent2, fixed_positions):
    child = [[0 for _ in range(9)] for _ in range(9)]

    for block_row in range(0, 9, 3):
        for block_col in range(0, 9, 3):
            source = parent1 if random.random() < 0.5 else parent2

            for i in range(3):
                for j in range(3):
                    x, y = block_row + i, block_col + j
                    if (x, y) in fixed_positions:
                        # Сохраняем фиксированную ячейку
                        child[x][y] = parent1[x][y]
                    else:
                        child[x][y] = source[x][y]
                        
    return child
# ========================== crossing
# ========================== mutation data
def get_bad_rows(individual):
    rows_nums = []
    for i in range(len(individual)):
        if len(set(individual[i])) < 9:
            rows_nums.append(i) 

    return rows_nums
# ========================== mutation data

def genetic_algorithm(population, fixed_positions, generations=10000, population_size=100, mutation_rate=0.55):
    best_fitness_values = []

    for generation in range(generations):
        population = sorted(population, key=fitness_full, reverse=True)
        best = population[0]
        best_fitness = fitness_full(best)
        best_fitness_values.append(best_fitness)

        print(f"Generation {generation}, Best fitness: {best_fitness}")
        if best_fitness == 243:
            print("Sudoku solved!")
            plot_progress(best_fitness_values)
            return best

        selected = group_tournament_selection(population)

        next_generation = []
        while len(next_generation) < population_size:
            parent1, parent2 = random.sample(selected, 2)
            child = uniform_crossover_sq(parent1, parent2, fixed_positions)

            if random.random() < mutation_rate:
                random_mutation(child, fixed_positions)

            next_generation.append(child)

        population = next_generation

    print("Max generations reached.")
    plot_progress(best_fitness_values)
    return max(population, key=fitness_full)

# Функция построения графика
def plot_progress(fitness_values):
    plt.figure(figsize=(10, 5))
    plt.plot(fitness_values, label='Best Fitness')
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.title("Best Fitness per Generation")
    plt.legend()
    plt.grid(True)
    plt.show()




def main():
    print(FIELD_SIZE)
    print(POPULATION_SIZE)
    print(P_CROSSOVER)
    print(P_MUTATION)
    print(MAX_GENERATIONS)

if __name__ == "__main__":
    field_creator = FieldCreator()
    field_creator.ReadFromFile('example.txt')
    # # print(field_creator.insert_list)
    population = field_creator.GeneratePopulation(200)

    print(get_bad_rows(test))
    # for ind in population:
    #     print(fitness_full(ind))
    
    # one_point_crossing_sq(population[0], population[1], field_creator.insert_list_indexes)

    # for item in population:
    #     print('\n'.join([' '.join(list(map(str, item[i]))) for i in range(9)]) + '\n')
    # print(fitness_full(test))

    # solution = genetic_algorithm(population, field_creator.insert_list_indexes, 10000, 200)
    # print(fitness_full(solution))
    # for row in solution:
    #     print(row)