from Modules.solution import Solution

FIELD_SIZE = 9
POPULATION_SIZE = 200
P_CROSSOVER = 0.5
P_MUTATION = 0.5
MAX_GENERATIONS = 150

if __name__ == "__main__":
    sol = Solution(1, 3, FIELD_SIZE)
    print(sol.id)
