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


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("ГА Судоку")
        self.setGeometry(300, 250, 350, 200)

        self.start_btn = QtWidgets.QPushButton(self)
        self.start_btn.setText("Запуск")
        self.start_btn.setFixedWidth(200)
        self.start_btn.clicked.connect(self.main)

    def main(self):
        print('ЗАПУЩЕНО')


# def evaluate():
# def crossover():
# def grade():

def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()
