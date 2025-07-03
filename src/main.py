from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
import random
import sys
from sudoku_field import *
from mutation import *
import matplotlib.pyplot as plt
from data_saver import *

test = [
    [5, 9, 3, 8, 1, 9, 6, 7, 2],
[8, 2, 4, 6, 3, 7, 5, 1, 4],
[6, 1, 7, 4, 5, 2, 8, 3, 9],
[1, 3, 5, 7, 2, 8, 4, 9, 6],
[4, 8, 9, 5, 6, 3, 7, 2, 1],
[7, 6, 2, 1, 9, 4, 3, 8, 5],
[9, 4, 6, 3, 7, 1, 2, 5, 8],
[3, 5, 1, 2, 8, 6, 9, 4, 7],
[2, 7, 8, 9, 4, 5, 1, 6, 3],
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
            source = parent1 if random.random() < 0.55 else parent2

            for i in range(3):
                for j in range(3):
                    x, y = block_row + i, block_col + j
                    if (x, y) in fixed_positions:
                        # Сохраняем фиксированную ячейку
                        child[x][y] = parent1[x][y]
                    else:
                        child[x][y] = source[x][y]
                        
    return child

def uniform_crossover_cell(parent1, parent2, fixed_positions):
    child = [row.copy() for row in parent1] 

    for i in range(9):
        for j in range(9):
            if (i, j) in fixed_positions:
                continue 
            
            child[i][j] = parent1[i][j] if random.random() < 0.5 else parent2[i][j]

    return child

# ========================== crossing
# ========================== mutation data
def get_bad_rows(individual):
    low_fitness_rows = []

    for i in range(9):
        row_fitness = 0
        for j in range(9):
            val = individual[i][j]

            fitness = 0

            if individual[i].count(val) == 1:
                fitness += 1

            column = [individual[x][j] for x in range(9)]
            if column.count(val) == 1:
                fitness += 1

            block_i = (i // 3) * 3
            block_j = (j // 3) * 3
            block = [individual[x][y] for x in range(block_i, block_i + 3)
                                  for y in range(block_j, block_j + 3)]
            if block.count(val) == 1:
                fitness += 1

            row_fitness += fitness

        if row_fitness < 27:
            low_fitness_rows.append(i)

    return low_fitness_rows

def get_bad_columns(individual):
    columns_indexes = []
    for j in range(9):
        column = []
        for i in range(len(individual)):
            column.append(individual[i][j])
        # if len(set(column)) < 9:
        print(column)
            # columns_indexes.append(j)

    # return columns_indexes
        
# ========================== mutation data

def genetic_algorithm(population, fixed_positions, generations=10000, population_size=100, mutation_rate=0.6):
    best_fitness_values = []
    data_init()

    for generation in range(generations):
        population = sorted(population, key=fitness_full, reverse=True)
        best = population[0]
        best_fitness = fitness_full(best)
        best_fitness_values.append(best_fitness)

        # Сохранение данных о поколении
        data = [best_fitness, field_to_str(best)]
        save_data(generation, data)

        print(f"Generation {generation}, Best fitness: {best_fitness}")
        if best_fitness == 243:
            print("Sudoku solved!")
            plot_progress(best_fitness_values)
            return best

        selected = group_tournament_selection(population, 4)

        next_generation = []
        while len(next_generation) < population_size:
            parent1, parent2 = random.sample(selected, 2)

            child = []
            # child = one_point_crossing_sq(parent1, parent2, fixed_positions)
            # child1 = uniform_crossover_cell(parent1, parent2, fixed_positions)
            # child2 = uniform_crossover_cell(parent1, parent2, fixed_positions)
            # child3 = uniform_crossover_cell(parent1, parent2, fixed_positions)
            cross_mode = random.choice(1,2,3)
            if cross_mode == 1:
                child = self.uniform_crossover_sq(parent1, parent2)
            if cross_mode == 2:
                child = self.uniform_crossover_row(parent1, parent2)
            if cross_mode == 3:
                child = self.uniform_crossover_column(parent1, parent2)

            if random.random() < mutation_rate:
                # if len(get_bad_rows(child)) > 0:
                #     mutation_among_bad_rows(child, fixed_positions, get_bad_rows(child), True)
                # else:
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

def main_start(field: list[list[str]], population_size: int, generation_size: int, p_mutation: float):
    field_creator = FieldCreator()
    field_creator.ReadFromList(field)
    population = field_creator.GeneratePopulation(population_size)
    solution = genetic_algorithm(population, field_creator.insert_list_indexes, generation_size, population_size, p_mutation)

if __name__ == "__main__":
    field_creator = FieldCreator()
    field_creator.ReadFromFile('example.txt')
    # # print(field_creator.insert_list)
    population = field_creator.GeneratePopulation(500)

    # print(get_bad_rows(test))

    # for ind in population:
    #     print(fitness_full(ind))
    
    # one_point_crossing_sq(population[0], population[1], field_creator.insert_list_indexes)

    # for item in population:
    #     print('\n'.join([' '.join(list(map(str, item[i]))) for i in range(9)]) + '\n')
    # print(fitness_full(test))

    solution = genetic_algorithm(population, field_creator.insert_list_indexes, 10000, 500)
    print(fitness_full(solution))
    for row in solution:
        print(row)