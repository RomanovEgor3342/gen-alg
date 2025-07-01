from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets
from main import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 660)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(820, 660))
        MainWindow.setMaximumSize(QtCore.QSize(820, 660))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(235, 236, 236);\n"
                                 "color: rgb(48, 48, 48);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # --- Вывод лучшего результата ---
        self.screen = QtWidgets.QLabel(self.centralwidget)
        self.screen.setGeometry(QtCore.QRect(510, 10, 300, 300))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setUnderline(True)
        self.screen.setFont(font)
        self.screen.setStyleSheet("border-color: rgb(220, 222, 221);\n"
                                  "background-color: rgb(230, 231, 231);\n"
                                  "color: rgb(99, 99, 99);\n"
                                  "border-radius: 10px;")
        self.screen.setAlignment(QtCore.Qt.AlignCenter)
        self.screen.setObjectName("screen")

        # --- Таблица ---
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(310, 10, 190, 300))
        self.tableWidget.setStyleSheet("border-color: rgb(220, 222, 221);\n"
                                       "background-color: rgb(230, 231, 231);\n"
                                       "color: rgb(27, 28, 28);\n"
                                       "border-radius: 10px;")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setHorizontalHeaderLabels(["Номер поколения"])
        self.tableWidget.setColumnWidth(0, 30)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # --- График ---
        self.graph = QtWidgets.QWidget()
        self.graph.setParent(self.centralwidget)  # добавляем график на центральный виджет!
        self.graph.setGeometry(QtCore.QRect(310, 320, 500, 330))
        self.graph.setStyleSheet("border-color: rgb(220, 222, 221);\n"
                                 "background-color: rgb(230, 231, 231);\n"
                                 "color: rgb(27, 28, 28);\n"
                                 "border-radius: 10px;")
        self.graph_layout = QtWidgets.QVBoxLayout(self.graph)

        # --- Группа параметров ---
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 300, 660))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-color: rgb(228, 229, 229);\n"
                                    "border-right-color: rgb(177, 179, 179);\n"
                                    "color: rgb(48, 48, 48);")
        self.groupBox.setTitle("Параметры")
        self.groupBox.setMaximumSize(QtCore.QSize(300, 660))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("\n"
                                    "background-color: rgb(228, 229, 229);\n"
                                    "border-right-color: rgb(177, 179, 179);\n"
                                    "color: rgb(48, 48, 48);\n"
                                    "selection-color: rgb(255, 255, 255);\n"
                                    "selection-background-color: rgb(16, 81, 193);")
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.groupBox.setObjectName("groupBox")

        # --- Кнопка запуска ---
        self.start_btn = QtWidgets.QPushButton(self.groupBox)
        self.start_btn.setGeometry(QtCore.QRect(72, 610, 100, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_btn.sizePolicy().hasHeightForWidth())
        self.start_btn.setSizePolicy(sizePolicy)
        self.start_btn.setMinimumSize(QtCore.QSize(100, 30))
        self.start_btn.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.start_btn.setFont(font)
        self.start_btn.setStyleSheet("""
            QPushButton {
                background-color: rgb(239, 240, 244);
                border-color: rgb(147, 147, 147);
                color: rgb(20, 21, 21);
                selection-color: rgb(255, 255, 255);
                selection-background-color: rgb(16, 81, 193);
                border-radius: 10px;
            }
            QPushButton:pressed {
                background-color: rgb(200, 200, 200); /* более тёмный цвет для затемнения */
            }
        """)
        self.start_btn.setObjectName("start_btn")

        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(178, 610, 50, 30))
        self.pushButton.setMinimumSize(QtCore.QSize(50, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(50, 30))
        self.pushButton.setStyleSheet("""
            QPushButton {
                background-color: rgb(239, 240, 244);
                border-color: rgb(147, 147, 147);
                color: rgb(20, 21, 21);
                selection-color: rgb(255, 255, 255);
                selection-background-color: rgb(16, 81, 193);
                border-radius: 10px;
            }
            QPushButton:pressed {
                background-color: rgb(200, 200, 200); /* более тёмный цвет для затемнения */
            }
        """)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(233, 610, 30, 30))
        self.pushButton_2.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("""
            QPushButton {
                background-color: rgb(239, 240, 244);
                border-color: rgb(147, 147, 147);
                color: rgb(20, 21, 21);
                selection-color: rgb(255, 255, 255);
                selection-background-color: rgb(16, 81, 193);
                border-radius: 10px;
            }
            QPushButton:pressed {
                background-color: rgb(200, 200, 200); /* более тёмный цвет для затемнения */
            }
        """)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(37, 610, 30, 30))
        self.pushButton_3.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("""
            QPushButton {
                background-color: rgb(239, 240, 244);
                border-color: rgb(147, 147, 147);
                color: rgb(20, 21, 21);
                selection-color: rgb(255, 255, 255);
                selection-background-color: rgb(16, 81, 193);
                border-radius: 10px;
            }
            QPushButton:pressed {
                background-color: rgb(200, 200, 200); /* более тёмный цвет для затемнения */
            }
        """)
        self.pushButton_3.setObjectName("pushButton_3")

        # --- Кнопка ---
        self.spin_mutation = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.spin_mutation.setGeometry(QtCore.QRect(230, 460, 55, 24))
        self.spin_mutation.setMaximumSize(QtCore.QSize(55, 16777215))
        self.spin_mutation.setStyleSheet("background-color: rgb(239, 240, 244);\n"
                                         "border-color: rgb(147, 147, 147);\n"
                                         "color: rgb(20, 21, 21);\n"
                                         "selection-color: rgb(255, 255, 255);\n"
                                         "selection-background-color: rgb(16, 81, 193);\n"
                                         "border-radius: 5px;")
        self.spin_mutation.setObjectName("spin_mutation")

        # --- Кнопка ---
        self.spin_crossover = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.spin_crossover.setGeometry(QtCore.QRect(230, 420, 55, 24))
        self.spin_crossover.setMaximumSize(QtCore.QSize(55, 16777215))
        self.spin_crossover.setStyleSheet("background-color: rgb(239, 240, 244);\n"
                                          "border-color: rgb(147, 147, 147);\n"
                                          "color: rgb(20, 21, 21);\n"
                                          "selection-color: rgb(255, 255, 255);\n"
                                          "selection-background-color: rgb(16, 81, 193);\n"
                                          "border-radius: 5px;")
        self.spin_crossover.setObjectName("spin_crossover")

        # Настройки для spin_mutation
        self.spin_mutation.setDecimals(2)
        self.spin_mutation.setRange(0.01, 0.99)
        self.spin_mutation.setSingleStep(0.01)

        # Настройки для spin_crossover
        self.spin_crossover.setDecimals(2)
        self.spin_crossover.setRange(0.01, 0.99)
        self.spin_crossover.setSingleStep(0.01)

        self.label_mutation = QtWidgets.QLabel(self.groupBox)
        self.label_mutation.setGeometry(QtCore.QRect(20, 460, 200, 20))
        self.label_mutation.setMinimumSize(QtCore.QSize(200, 20))
        self.label_mutation.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_mutation.setFont(font)
        self.label_mutation.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_mutation.setObjectName("label_mutation")

        self.label_crossover = QtWidgets.QLabel(self.groupBox)
        self.label_crossover.setGeometry(QtCore.QRect(20, 420, 200, 20))
        self.label_crossover.setMinimumSize(QtCore.QSize(200, 20))
        self.label_crossover.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_crossover.setFont(font)
        self.label_crossover.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_crossover.setObjectName("label_crossover")

        self.label_population = QtWidgets.QLabel(self.groupBox)
        self.label_population.setGeometry(QtCore.QRect(20, 340, 200, 20))
        self.label_population.setMinimumSize(QtCore.QSize(200, 20))
        self.label_population.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_population.setFont(font)
        self.label_population.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_population.setObjectName("label_population")

        self.label_max = QtWidgets.QLabel(self.groupBox)
        self.label_max.setGeometry(QtCore.QRect(20, 300, 200, 20))
        self.label_max.setMinimumSize(QtCore.QSize(200, 20))
        self.label_max.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_max.setFont(font)
        self.label_max.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_max.setObjectName("label_max")

        self.enter_population_size = QtWidgets.QLineEdit(self.groupBox)
        self.enter_population_size.setGeometry(QtCore.QRect(240, 340, 40, 21))
        self.enter_population_size.setMaximumSize(QtCore.QSize(40, 16777215))
        self.enter_population_size.setStyleSheet("background-color: rgb(239, 240, 244);\n"
                                                 "border-color: rgb(147, 147, 147);\n"
                                                 "color: rgb(20, 21, 21);\n"
                                                 "selection-color: rgb(255, 255, 255);\n"
                                                 "selection-background-color: rgb(16, 81, 193);\n"
                                                 "border-radius: 5px;")
        self.enter_population_size.setObjectName("enter_population_size")

        self.enter_max = QtWidgets.QLineEdit(self.groupBox)
        self.enter_max.setGeometry(QtCore.QRect(240, 300, 40, 21))
        self.enter_max.setMaximumSize(QtCore.QSize(40, 16777215))
        self.enter_max.setStyleSheet("background-color: rgb(239, 240, 244);\n"
                                     "border-color: rgb(147, 147, 147);\n"
                                     "color: rgb(20, 21, 21);\n"
                                     "selection-color: rgb(255, 255, 255);\n"
                                     "selection-background-color: rgb(16, 81, 193);\n"
                                     "border-radius: 5px;")
        self.enter_max.setObjectName("enter_max")

        self.label_population_2 = QtWidgets.QLabel(self.groupBox)
        self.label_population_2.setGeometry(QtCore.QRect(20, 380, 200, 20))
        self.label_population_2.setMinimumSize(QtCore.QSize(200, 20))
        self.label_population_2.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_population_2.setFont(font)
        self.label_population_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_population_2.setObjectName("label_population_2")
        self.enter_population_size_2 = QtWidgets.QLineEdit(self.groupBox)
        self.enter_population_size_2.setGeometry(QtCore.QRect(240, 380, 40, 21))
        self.enter_population_size_2.setMaximumSize(QtCore.QSize(40, 16777215))
        self.enter_population_size_2.setStyleSheet("background-color: rgb(239, 240, 244);\n"
                                                   "border-color: rgb(147, 147, 147);\n"
                                                   "color: rgb(20, 21, 21);\n"
                                                   "selection-color: rgb(255, 255, 255);\n"
                                                   "selection-background-color: rgb(16, 81, 193);\n"
                                                   "border-radius: 5px;")
        self.enter_population_size_2.setObjectName("enter_population_size_2")

        # Ограничение ввода только чисел от 0 до 10000
        int_validator = QtGui.QIntValidator(0, 10000)
        self.enter_population_size.setValidator(int_validator)
        self.enter_max.setValidator(int_validator)
        self.enter_population_size_2.setValidator(int_validator)

        self.tablescreen = QtWidgets.QTableWidget(self.groupBox)
        self.tablescreen.setGeometry(QtCore.QRect(40, 60, 220, 220))
        self.tablescreen.setMinimumSize(QtCore.QSize(220, 220))
        self.tablescreen.setMaximumSize(QtCore.QSize(220, 220))
        self.tablescreen.setObjectName("tablescreen")
        rows, cols = 9, 9
        self.tablescreen.setRowCount(rows)
        self.tablescreen.setColumnCount(cols)
        cell_size = 24
        for i in range(rows):
            self.tablescreen.setRowHeight(i, cell_size)
        for j in range(cols):
            self.tablescreen.setColumnWidth(j, cell_size)
        for i in range(rows):
            for j in range(cols):
                item = QtWidgets.QTableWidgetItem("x")
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tablescreen.setItem(i, j, item)
        self.tablescreen.horizontalHeader().setVisible(False)
        self.tablescreen.verticalHeader().setVisible(False)
        self.tablescreen.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)

        self.label_f = QtWidgets.QLabel(self.groupBox)
        self.label_f.setGeometry(QtCore.QRect(90, 30, 110, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_f.setFont(font)
        self.label_f.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                   "color: rgb(48, 48, 48);")
        self.label_f.setAlignment(QtCore.Qt.AlignCenter)
        self.label_f.setObjectName("label_f")

        self.error_label = QtWidgets.QLabel(self.groupBox)
        self.error_label.setGeometry(QtCore.QRect(0, 570, 300, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.error_label.setFont(font)
        self.error_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.error_label.setAlignment(QtCore.Qt.AlignCenter)
        self.error_label.setObjectName("error_label")

        # --- Подпись к результату ---
        self.label = QtWidgets.QLabel("Лучший результат", self.centralwidget)
        self.label.setGeometry(QtCore.QRect(600, 30, 121, 16))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0, 0);")
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Подключение обработчиков
        self.functions()

    # --- Обработчик выбора строки ---
    def on_row_clicked(self):
        row = self.tableWidget.currentRow()
        key = self.tableWidget.item(row, 0).text()
        label_text = (self.data.get(key))[1]
        self.screen.setText(label_text)

    # --- Обновить таблицу ---
    def update_table(self, table):
        self.data = table
        self.tableWidget.setRowCount(len(self.data))
        for row, (key, value) in enumerate(self.data.items()):
            item1 = QtWidgets.QTableWidgetItem(key)
            item1.setTextAlignment(QtCore.Qt.AlignCenter)
            item2 = QtWidgets.QTableWidgetItem(value[0])
            item2.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(row, 0, item1)
            self.tableWidget.setItem(row, 1, item2)

    # --- Отрисовщик графика ---
    def plot_graph(self, x_data, y1, y2):
        if hasattr(self, 'canvas'):
            self.graph_layout.removeWidget(self.canvas)
            self.canvas.setParent(None)

        background_color = (23 / 255, 23 / 255, 26 / 255)
        spine_color = (174 / 255, 176 / 255, 183 / 255)

        figure = Figure(figsize=(5, 3), tight_layout=True)
        self.canvas = FigureCanvas(figure)
        ax = figure.add_subplot(111)
        ax.plot(x_data, y1, color='red', label='1', marker='o')
        ax.plot(x_data, y2, color='blue', label='2', marker='o')
        ax.set_title("График", color=spine_color)
        ax.set_xlabel("X", color=spine_color)
        ax.set_ylabel("Y", color=spine_color)
        figure.patch.set_facecolor(background_color)
        ax.set_facecolor(background_color)
        ax.legend(facecolor=background_color, edgecolor=spine_color, labelcolor=spine_color)
        ax.tick_params(colors=spine_color)
        for spine in ax.spines.values():
            spine.set_color(spine_color)

        self.graph_layout.addWidget(self.canvas)

    # --- Перевод интерфейса ---
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ГА Судоку"))
        self.groupBox.setTitle(_translate("MainWindow", "Параметры"))
        self.start_btn.setText(_translate("MainWindow", "Запуск"))
        self.label_mutation.setText(_translate("MainWindow", "Вероятность мутации"))
        self.label_crossover.setText(_translate("MainWindow", "Вероятность скрещивания"))
        self.label_population.setText(_translate("MainWindow", "Размер популяции"))
        self.label_max.setText(_translate("MainWindow", "Макс. кол-во поколений"))
        self.label_f.setText(_translate("MainWindow", "Начальное поле"))
        self.error_label.setText(_translate("MainWindow", ""))
        self.label.setText(_translate("MainWindow", "Лучший результат"))
        self.pushButton.setText(_translate("MainWindow", "Стоп"))
        self.pushButton_2.setText(_translate("MainWindow", "ᐅ"))
        self.label_population_2.setText(_translate("MainWindow", "Кол-во случайных клеток"))
        self.pushButton_3.setText(_translate("MainWindow", "ᐊ"))

    # --- Обработчик функций ---
    def functions(self):
        self.tableWidget.clicked.connect(lambda: self.on_row_clicked())
        self.start_btn.clicked.connect(lambda: self.start())

    # --- Обработчик запуска ---
    def start(self):
        print("Программа запущена")

        x = list(range(10))
        y1 = [i ** 2 for i in x]
        y2 = [i * 3 for i in x]
        self.plot_graph(x, y1, y2)

    def stop(self):
        print("Программа остановлена")


data = {
    "1": ["data", "1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9\n" * 9],
    "2": ["data", "9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1\n" * 9],
    "3": ["data", "0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0\n" * 9]
}

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.update_table(data)
    sys.exit(app.exec_())
