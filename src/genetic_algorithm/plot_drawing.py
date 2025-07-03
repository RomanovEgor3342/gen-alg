import matplotlib.pyplot as plt

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