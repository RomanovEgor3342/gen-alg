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


def main():
    print(FIELD_SIZE)
    print(POPULATION_SIZE)
    print(P_CROSSOVER)
    print(P_MUTATION)
    print(MAX_GENERATIONS)


if __name__ == "__main__":
    print("Запущено")