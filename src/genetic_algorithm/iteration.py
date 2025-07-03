def one_iteration(self, population_size, mutation_rate):

    # /finding best fitness
    population = sorted(self.population, key=self.fitness_full, reverse=True)
    best = population[0]
    best_fitness = self.fitness_full(best)
    self.best_fitness_values.append(best_fitness)

    # /Сохранение данных о поколении
    data = [best_fitness, field_to_str(best)]
    save_data(generation, data)

    #/ printing debug data
    print(
        f"Generation {generation}, Best fitness: {best_fitness}, diversity: {calculate_population_diversity(population)}")
    # print(f"Generation {generation}, Best fitness: {best_fitness}, diversity: ")
    if best_fitness == 243:
        print("Sudoku solved!")
        plot_progress(self.best_fitness_values)
        return best

    #/ selection
    selected = self.group_tournament_selection(10)

    #/ best 5% of selected generation survives
    next_generation = population[:math.ceil(0.05 * len(population))]
    # next_generation = []

    #/ crossing + mutation
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
        cross_mode = random.choice([1, 2, 3])
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

    #/ generating new population
    self.population = next_generation