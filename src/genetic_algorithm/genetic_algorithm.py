import random
import numpy as np
from typing import overload, Literal, Union
import math

from data_saver import *
from reader_writer import *
from plot_drawing import *
from new_crossing import *


class GeneticAlgorithm():
    def __init__(self):
        self.main_permutation = list(range(1, 10)) * 9
        self.insert_list_indexes = []
        self.insert_list_symbols = []
        self.population = []
        self.best_fitness_values = []

    # ========================== getting data
    @overload
    def get_data(self, data: list, flag: Literal['l']) -> None:
        ...
    @overload
    def get_data(self, data: str, flag: Literal['f']) -> None:
        ...
    def get_data(self, data: Union[list, str], flag: str) -> None:
        if flag == 'l' and isinstance(data, list):
            self.main_permutation, self.insert_list_indexes, self.insert_list_symbols = ReadFromList(data)
        elif flag == 'f' and isinstance(data, str):
            self.main_permutation, self.insert_list_indexes, self.insert_list_symbols = ReadFromFile(data)
        else:
            raise ValueError("Некорректные аргументы")
    # ==========================

    # ========================== generating population
    def GeneratePopulation(self, entities_amount: int) -> None:
        for _ in range(entities_amount):
            new_entity = np.random.permutation(self.main_permutation).tolist()
            for index in range(len(self.insert_list_symbols)):
                new_entity.insert(self.insert_list_indexes[index][0] * 9 + self.insert_list_indexes[index][1], self.insert_list_symbols[index])
            new_entity = [new_entity[i:i + 9] for i in range(0, 81, 9)]
            self.population.append(new_entity)
    # ==========================

    # ========================== fitness calculation
    def fitness_full(self, individual):
        amount = 0
        for line in individual:
            amount += len(set(line))

        for column in zip(*individual):
            amount += len(set(column))

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = [individual[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]

                amount += len(set(square))

        return amount


    def fitness_cut(self, individual):
        amount = 0
        for line in individual:
            if len(set(line)) == 9:
                amount += 1

        for column in zip(*individual):
            if len(set(column)) == 9:
                amount += 1

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = [individual[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]

                if len(set(square)) == 9:
                    amount += 1

        return amount
    # ==========================

    # ========================== selection
    def group_tournament_selection(self, k=2):
        random.shuffle(self.population)
        best_individuals = []

        for i in range(0, len(self.population), k):
            group = self.population[i:i + k]
            best_in_group = max(group, key = self.fitness_full)
            best_individuals.append(best_in_group)

        return best_individuals
    # ==========================

    # ========================== crossing
    def one_point_crossing_sq(self, parent1, parent2):
        child = [row.copy() for row in parent1]

        num_squares_to_swap = random.randint(1, 7)

        all_squares = [(i, j) for i in range(0, 9, 3) for j in range(0, 9, 3)]

        squares_to_swap = random.sample(all_squares, num_squares_to_swap)

        for block_row, block_col in squares_to_swap:
            for i in range(block_row, block_row + 3):
                for j in range(block_col, block_col + 3):

                    if (i, j) not in self.insert_list_indexes:
                        child[i][j] = parent2[i][j]

        return child

    def uniform_crossover_sq(self, parent1, parent2):
        child = [[0 for _ in range(9)] for _ in range(9)]

        for block_row in range(0, 9, 3):
            for block_col in range(0, 9, 3):
                source = parent1 if random.random() < 0.55 else parent2

                for i in range(3):
                    for j in range(3):
                        x, y = block_row + i, block_col + j
                        if (x, y) in self.insert_list_indexes:
                            # Сохраняем фиксированную ячейку
                            child[x][y] = parent1[x][y]
                        else:
                            child[x][y] = source[x][y]

        return child

    def uniform_crossover_cell(self, parent1, parent2):
        child = [row.copy() for row in parent1] 

        for i in range(9):
            for j in range(9):
                if (i, j) in self.insert_list_indexes:
                    continue 
                
                child[i][j] = parent1[i][j] if random.random() < 0.5 else parent2[i][j]

        return child

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
                for row in range(9):
                    child[row][column] = parent2[row][column]

        return child
    # ==========================

    # ========================== mutation
    def random_mutation(self, entity: list[list[int]]) -> None:
        numbers = list(range(0, 81))
        for item in self.insert_list_indexes:
            numbers.remove(item[0] * 9 + item[1])

        first_sum = random.choice(numbers)
        numbers.remove(first_sum)
        second_sum = random.choice(numbers)

        first_x = first_sum // 9
        first_y = first_sum % 9

        second_x = second_sum // 9
        second_y = second_sum % 9

        entity[first_x][first_y], entity[second_x][second_y] = entity[second_x][second_y], entity[first_x][first_y]

    def row_shuffle_mutation(self, entity: list[list[int]]) -> None:
        fixed_set = set(self.insert_list_indexes)
        row_idx = random.randint(0, 8)
        mutable_indices = [j for j in range(9) if (row_idx, j) not in fixed_set]
        
        if len(mutable_indices) < 2:
            return
        
        values_to_shuffle = [entity[row_idx][j] for j in mutable_indices]
        random.shuffle(values_to_shuffle)
        
        for idx, j in enumerate(mutable_indices):
            entity[row_idx][j] = values_to_shuffle[idx]

    def mutation_change_5_percent(self, entity: list[list[int]]) -> None:
        fixed_set = set(self.insert_list_indexes)

        mutable_positions = [(i, j) for i in range(9) for j in range(9) if (i, j) not in fixed_set]
        
        if not mutable_positions:
            return

        num_to_mutate = max(1, round(0.05 * len(mutable_positions)))

        positions_to_mutate = random.sample(mutable_positions, num_to_mutate)

        for i, j in positions_to_mutate:
            current_val = entity[i][j]
            new_val = random.choice([v for v in range(1, 10) if v != current_val])
            entity[i][j] = new_val
    # ==========================

    # ========================== main cycle
    def main_cycle(self, generations, population_size, mutation_rate):

        data_init()

        for generation in range(generations):
            population = sorted(self.population, key = self.fitness_full, reverse=True)
            best = population[0]
            best_fitness = self.fitness_full(best)
            self.best_fitness_values.append(best_fitness)

            # Сохранение данных о поколении
            data = [best_fitness, field_to_str(best)]
            save_data(generation, data)

            print(f"Generation {generation}, Best fitness: {best_fitness}, diversity: {calculate_population_diversity(population)}")
            # print(f"Generation {generation}, Best fitness: {best_fitness}, diversity: ")
            if best_fitness == 243:
                print("Sudoku solved!")
                plot_progress(self.best_fitness_values)
                return best

            selected = self.group_tournament_selection(2)

            # next_generation = population[:math.ceil(0.05 * len(population))]
            next_generation = []
            while len(next_generation) < population_size:
                parent1, parent2 = random.sample(selected, 2)
                # child = self.uniform_crossover_cell(parent1, parent2)
                # child = []
                # if random.random() < crossover_rate:
                # child = self.one_point_crossing_sq(parent1, parent2)

                # else:
                #     next_generation.append(parent1)
                #     next_generation.append(parent2)
                #     continue

                child = []
                # child = self.one_point_crossing_sq(parent1, parent2, fixed_positions)
            # child1 = uniform_crossover_cell(parent1, parent2, fixed_positions)
            # child2 = uniform_crossover_cell(parent1, parent2, fixed_positions)
            # child3 = uniform_crossover_cell(parent1, parent2, fixed_positions)
                cross_mode = random.choice([1,2,3])
                if cross_mode == 1:
                    child = self.uniform_crossover_sq(parent1, parent2)
                if cross_mode == 2:
                    child = self.uniform_crossover_row(parent1, parent2)
                if cross_mode == 3:
                    child = self.uniform_crossover_column(parent1, parent2)

                if (random_number := random.random()) < mutation_rate:
                    # self.row_shuffle_mutation(child)
                    self.random_mutation(child)

                    # if len(get_bad_rows(child)) > 0:
                    #     mutation_among_bad_rows(child, fixed_positions, get_bad_rows(child), True)
                    # else:

                # ВОТ СЮДА Я ДОБАВИЛ МЕГА РАНДОМНУЮ МУТАЦИЮ!!!!!!!!!!!!!!!!!!!
                # elif random_number < 0.05:
                #     child = self.very_random_mutation()



                next_generation.append(child)

            self.population = next_generation

        print("Max generations reached.")
        plot_progress(self.best_fitness_values)
        return max(self.population, key = self.fitness_full)
    # ==========================

    """
    ============================
    ТЕСТОВЫЕ ФУНКЦИИ АЛГОРИТМА
    ============================
    """
    def very_random_mutation(self) -> list[list[int]]:
        new_entity = np.random.permutation(self.main_permutation).tolist()
        for index in range(len(self.insert_list_symbols)):
            new_entity.insert(self.insert_list_indexes[index][0] * 9 + self.insert_list_indexes[index][1],
                              self.insert_list_symbols[index])
        new_entity = [new_entity[i:i + 9] for i in range(0, 81, 9)]

        return new_entity


# =========================================================
def main_start(field: list[list[str]], population_size: int, generation_size: int, p_mutation: float):
    gen_alg = GeneticAlgorithm()
    gen_alg.get_data(field, 'l')
    gen_alg.GeneratePopulation(population_size)
    solution = gen_alg.main_cycle(generation_size, population_size, p_mutation)

# ========================== print individual
def print_ind(ind):
    print('\n'.join([' '.join(list(map(str, ind[i]))) for i in range(9)]) + '\n')
# ==========================
def calculate_population_diversity(population: list[list[list[int]]]) -> float:

    def grid_to_hashable(grid):
        return tuple(tuple(row) for row in grid)
    
    unique_grids = set(grid_to_hashable(individual) for individual in population)
    total = len(population)
    
    if total == 0:
        return 0.0

    diversity_percent = (len(unique_grids) / total) * 100
    return diversity_percent
# ==========================


if __name__ == "__main__":
    gen_alg = GeneticAlgorithm()
    # gen_alg.insert_list_indexes =[(1, 1), (5, 6), (2, 8)]
    gen_alg.get_data('example.txt', 'f')
    gen_alg.GeneratePopulation(8000)

    solution = gen_alg.main_cycle(10000, 8000, 0.5)

    print(gen_alg.fitness_full(solution))
    print_ind(solution)