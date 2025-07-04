from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.figure import Figure
from genetic_algorithm import *



class UiMainWindow(object):
    def __init__(self):
        self.i = 0
        self.alg = GeneticAlgorithm()
        self.population_size = 0
        self.population = self.alg.GeneratePopulation(10)
        self.fixed_positions = 0
        self.generations = 0
        self.p_mutation = 0
        self.is_start = False
        self.figure = None
        self.ax = None
        self.line = None
        self.canvas = None
        self.is_pause = False

    def setup_ui(self, MainWindow):

        # ========================================
        #   Настройки окна
        # ========================================
        self.MainWindow = MainWindow
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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setStyleSheet("background-color: rgb(235, 236, 236);\n"
                                 "color: rgb(48, 48, 48);")

        # ========================================
        #   Окно вывода лучшего результата
        # ========================================
        self.screen = QtWidgets.QLabel(self.centralwidget)
        self.screen.setGeometry(QtCore.QRect(510, 10, 300, 300))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setUnderline(True)
        self.screen.setFont(font)
        self.screen.setAlignment(QtCore.Qt.AlignCenter)
        self.screen.setObjectName("screen")
        self.screen.setStyleSheet("border-color: rgb(220, 222, 221);\n"
                                  "background-color: rgb(230, 231, 231);\n"
                                  "color: rgb(99, 99, 99);\n"
                                  "border-radius: 10px;")

        # ========================================
        #   Таблица результатов
        # ========================================
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(310, 10, 190, 300))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["№", "Best fitness"])
        self.tableWidget.setColumnWidth(0, 60)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setStyleSheet("border-color: rgb(220, 222, 221);\n"
                                       "background-color: rgb(230, 231, 231);\n"
                                       "color: rgb(27, 28, 28);\n"
                                       "border-radius: 10px;")

        # ========================================
        #   График
        # ========================================
        self.graph = QtWidgets.QWidget()
        self.graph.setParent(self.centralwidget)
        self.graph.setGeometry(QtCore.QRect(310, 320, 500, 330))
        self.graph_layout = QtWidgets.QVBoxLayout(self.graph)
        self.graph.setStyleSheet("border-color: rgb(220, 222, 221);\n"
                                 "background-color: rgb(230, 231, 231);\n"
                                 "color: rgb(27, 28, 28);\n"
                                 "border-radius: 10px;")

        # ========================================
        #   Группа параметров
        # ========================================
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 300, 660))
        self.groupBox.setMinimumSize(QtCore.QSize(300, 660))
        self.groupBox.setMaximumSize(QtCore.QSize(300, 660))
        self.groupBox.setFont(font)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setStyleSheet("\n"
                                    "background-color: rgb(228, 229, 229);\n"
                                    "border-right-color: rgb(177, 179, 179);\n"
                                    "color: rgb(48, 48, 48);\n"
                                    "selection-color: rgb(255, 255, 255);\n"
                                    "selection-background-color: rgb(16, 81, 193);")

        # ========================================
        #   Кнопка запуска
        # ========================================
        self.start_btn = QtWidgets.QPushButton(self.groupBox)
        self.start_btn.setGeometry(QtCore.QRect(25, 610, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.start_btn.setFont(font)
        self.start_btn.setObjectName("start_btn")
        self.start_btn.setStyleSheet("QPushButton {background-color: rgb(239, 240, 244);"
                                     "border-color: rgb(147, 147, 147); color: rgb(20, 21, 21); "
                                     "selection-color: rgb(255, 255, 255);selection-background-color: rgb(16, 81, 193);"
                                     "border-radius: 10px} QPushButton:pressed {background-color: rgb(200, 200, 200)}")

        # ========================================
        #   Кнопка загрузить
        # ========================================
        self.download_btn = QtWidgets.QPushButton(self.groupBox)
        self.download_btn.setGeometry(QtCore.QRect(90, 290, 120, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.download_btn.setFont(font)
        self.download_btn.setObjectName("download_btn")
        self.download_btn.setStyleSheet("QPushButton {background-color: rgb(239, 240, 244);"
                                        "border-color: rgb(147, 147, 147); color: rgb(20, 21, 21); "
                                        "selection-color: rgb(255, 255, 255);"
                                        "selection-background-color: rgb(16, 81, 193);"
                                        "border-radius: 10px}"
                                        "QPushButton:pressed {background-color: rgb(200, 200, 200)}")

        # ========================================
        #   Вероятность мутации
        # ========================================
        self.label_mutation = QtWidgets.QLabel(self.groupBox)
        self.label_mutation.setGeometry(QtCore.QRect(20, 410, 200, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_mutation.setFont(font)
        self.label_mutation.setObjectName("label_mutation")
        self.label_mutation.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

        self.spin_mutation = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.spin_mutation.setGeometry(QtCore.QRect(230, 410, 55, 24))
        self.spin_mutation.setObjectName("spin_mutation")
        self.spin_mutation.setStyleSheet("background-color: rgb(239, 240, 244);\n"
                                         "border-color: rgb(147, 147, 147);\n"
                                         "color: rgb(20, 21, 21);\n"
                                         "selection-color: rgb(255, 255, 255);\n"
                                         "selection-background-color: rgb(16, 81, 193);\n"
                                         "border-radius: 5px;")

        self.spin_mutation.setDecimals(2)
        self.spin_mutation.setRange(0.01, 0.99)
        self.spin_mutation.setSingleStep(0.01)

        # ========================================
        #   Размер популяции
        # ========================================
        self.label_population = QtWidgets.QLabel(self.groupBox)
        self.label_population.setGeometry(QtCore.QRect(20, 370, 200, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_population.setFont(font)
        self.label_population.setObjectName("label_population")
        self.label_population.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

        self.enter_population_size = QtWidgets.QLineEdit(self.groupBox)
        self.enter_population_size.setGeometry(QtCore.QRect(240, 370, 40, 21))
        self.enter_population_size.setObjectName("enter_population_size")
        self.enter_population_size.setStyleSheet("background-color: rgb(239, 240, 244);\n"
                                                 "border-color: rgb(147, 147, 147);\n"
                                                 "color: rgb(20, 21, 21);\n"
                                                 "selection-color: rgb(255, 255, 255);\n"
                                                 "selection-background-color: rgb(16, 81, 193);\n"
                                                 "border-radius: 5px;")

        int_validator = QtGui.QIntValidator(0, 10000)
        self.enter_population_size.setValidator(int_validator)

        # ========================================
        #   Панель управдения
        # ========================================
        self.label_bar = QtWidgets.QLabel(self.groupBox)
        self.label_bar.setGeometry(QtCore.QRect(130, 610, 145, 30))
        self.label_bar.setStyleSheet("background-color: rgb(187, 188, 188);\n"
                                     "border-color: rgb(147, 147, 147);\n"
                                     "color: rgb(20, 21, 21);\n"
                                     "selection-color: rgb(255, 255, 255);\n"
                                     "selection-background-color: rgb(16, 81, 193);\n"
                                     "border-radius: 10px;")
        self.label_bar.setText("")
        self.label_bar.setObjectName("label_bar")
        self.label_bar.raise_()

        # ========================================
        #   Кнопка паузы
        # ========================================
        self.pause = QtWidgets.QPushButton(self.groupBox)
        self.pause.setGeometry(QtCore.QRect(130, 610, 30, 30))
        self.pause.setMinimumSize(QtCore.QSize(30, 30))
        self.pause.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.pause.setFont(font)
        self.pause.setEnabled(False)
        self.pause.setObjectName("pause")
        self.pause.setStyleSheet("QPushButton {background-color: rgb(187, 188, 188);"
                                 "border-color: rgb(147, 147, 147); color: rgb(20, 21, 21); "
                                 "selection-color: rgb(255, 255, 255);"
                                 "selection-background-color: rgb(16, 81, 193);"
                                 "border-radius: 10px}")

        # ========================================
        #   Макс. кол-во поколений
        # ========================================
        self.label_max = QtWidgets.QLabel(self.groupBox)
        self.label_max.setGeometry(QtCore.QRect(20, 330, 200, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_max.setFont(font)
        self.label_max.setObjectName("label_max")
        self.label_max.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

        self.enter_max = QtWidgets.QLineEdit(self.groupBox)
        self.enter_max.setGeometry(QtCore.QRect(240, 330, 40, 21))
        self.enter_max.setObjectName("enter_max")
        self.enter_max.setStyleSheet("background-color: rgb(239, 240, 244);\n"
                                     "border-color: rgb(147, 147, 147);\n"
                                     "color: rgb(20, 21, 21);\n"
                                     "selection-color: rgb(255, 255, 255);\n"
                                     "selection-background-color: rgb(16, 81, 193);\n"
                                     "border-radius: 5px;")

        self.enter_max.setValidator(int_validator)

        # ========================================
        #   Таблица для ввода старта
        # ========================================
        self.label_f = QtWidgets.QLabel(self.groupBox)
        self.label_f.setGeometry(QtCore.QRect(90, 30, 110, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_f.setFont(font)
        self.label_f.setAlignment(QtCore.Qt.AlignCenter)
        self.label_f.setObjectName("label_f")
        self.label_f.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                   "color: rgb(48, 48, 48);")

        self.tablescreen = QtWidgets.QTableWidget(self.groupBox)
        self.tablescreen.setGeometry(QtCore.QRect(40, 60, 220, 220))
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

        # ========================================
        #   Вывод ошибки
        # ========================================
        self.error_label = QtWidgets.QLabel(self.groupBox)
        self.error_label.setGeometry(QtCore.QRect(0, 530, 300, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.error_label.setFont(font)
        self.error_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.error_label.setAlignment(QtCore.Qt.AlignCenter)
        self.error_label.setObjectName("error_label")

        # ========================================
        #   Кнопка включить до результата
        # ========================================
        self.to_end = QtWidgets.QPushButton(self.groupBox)
        self.to_end.setGeometry(QtCore.QRect(165, 610, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.to_end.setFont(font)
        self.to_end.setObjectName("to_end")
        self.to_end.setEnabled(False)
        self.to_end.setStyleSheet("QPushButton {background-color: rgb(187, 188, 188);"
                                  "border-color: rgb(147, 147, 147); color: rgb(20, 21, 21); "
                                  "selection-color: rgb(255, 255, 255);"
                                  "selection-background-color: rgb(16, 81, 193);"
                                  "border-radius: 10px}")

        # ========================================
        #   Шкала выполнения
        # ========================================
        self.progressBar = QtWidgets.QProgressBar(self.groupBox)
        self.progressBar.setGeometry(QtCore.QRect(50, 580, 201, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("background-color: rgb(213, 215, 213, 0)")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.progressBar.setObjectName("progressBar")

        # ========================================
        #   Кнопка один шаг
        # ========================================
        self.one_step = QtWidgets.QPushButton(self.groupBox)
        self.one_step.setGeometry(QtCore.QRect(240, 610, 35, 30))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.one_step.setFont(font)
        self.one_step.setObjectName("one_step")
        self.one_step.setEnabled(False)
        self.one_step.setStyleSheet("QPushButton {background-color: rgb(187, 188, 188);"
                                    "border-color: rgb(147, 147, 147); color: rgb(20, 21, 21);"
                                    "selection-color: rgb(255, 255, 255);"
                                    "selection-background-color: rgb(16, 81, 193);"
                                    "border-radius: 10px}")

        # ========================================
        #   Обработчики
        # ========================================
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.functions()

    # ========================================
    #   Перевод интерфейса
    # ========================================
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ГА Судоку"))
        self.groupBox.setTitle(_translate("MainWindow", "Параметры"))
        self.start_btn.setText(_translate("MainWindow", "Старт"))
        self.label_mutation.setText(_translate("MainWindow", "Вероятность мутации"))
        self.label_population.setText(_translate("MainWindow", "Размер популяции"))
        self.label_max.setText(_translate("MainWindow", "Макс. кол-во поколений"))
        self.label_f.setText(_translate("MainWindow", "Начальное поле"))
        self.error_label.setText(_translate("MainWindow", ""))
        self.download_btn.setText(_translate("MainWindow", "Загрузить файл"))
        self.to_end.setText(_translate("MainWindow", "⏩"))
        self.pause.setText(_translate("MainWindow", "⏸"))
        self.one_step.setText(_translate("MainWindow", "+1"))

    # ========================================
    #   Обработчик выбора строки
    # ========================================
    def on_row_clicked(self):
        row = self.tableWidget.currentRow()
        key = self.tableWidget.item(row, 0).text()
        label_text = format_9x9_square(str_to_field((self.data.get(key))[1]))
        self.screen.setText(label_text)
        print(self.data.get('best_fitness')[:int(key)])
        self.plot_graph(self.data.get('best_fitness')[:int(key)])

    # ========================================
    #   Обновление таблицы
    # ========================================
    def update_table(self):
        self.data = read_data()
        keys = list(self.data.keys())[1:]
        self.tableWidget.setRowCount(len(keys))
        for row, key in enumerate(keys):
            value = self.data[key]
            item1 = QtWidgets.QTableWidgetItem(str(key))
            item1.setTextAlignment(QtCore.Qt.AlignCenter)
            item2 = QtWidgets.QTableWidgetItem(str(value[0]) if value else "")
            item2.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(row, 0, item1)
            self.tableWidget.setItem(row, 1, item2)

    # ========================================
    #   Обновление экрана результата
    # ========================================
    def update_screen(self, array):
        for i in range(9):
            for j in range(9):
                item = QtWidgets.QTableWidgetItem(array[i][j])
                self.tablescreen.setItem(i, j, item)

    # ========================================
    #   Отрисовщик графика
    # ========================================
    # def plot_graph(self, fitness_values):
    #     if hasattr(self, 'canvas'):
    #         self.graph_layout.removeWidget(self.canvas)
    #         self.canvas.setParent(None)

    #     figure = Figure(figsize=(10, 5), tight_layout=True)
    #     figure.patch.set_facecolor((224 / 255, 225 / 255, 225 / 255))
    #     self.canvas = FigureCanvas(figure)
    #     ax = figure.add_subplot(111)
    #     ax.set_facecolor((224 / 255, 225 / 255, 225 / 255))

    #     ax.plot(fitness_values, label='Best Fitness')
    #     ax.set_xlabel("Generation")
    #     ax.set_ylabel("Fitness")
    #     ax.set_title("Best Fitness per Generation")
    #     ax.legend()
    #     ax.grid(True)

    #     self.graph_layout.addWidget(self.canvas)

    def plot_graph(self, fitness_values):
        # Если график ещё не инициализирован
        if not hasattr(self, 'canvas') or self.canvas is None:
            self.figure = Figure(figsize=(10, 5), tight_layout=True)
            self.figure.patch.set_facecolor((224/255, 225/255, 225/255))
            
            self.canvas = FigureCanvas(self.figure)
            self.ax = self.figure.add_subplot(111)
            self.ax.set_facecolor((224/255, 225/255, 225/255))
            
            self.graph_layout.addWidget(self.canvas)
            self.canvas.show()

        self.ax.clear()
        self.ax.plot(fitness_values, label='Best Fitness')
        self.ax.set_xlabel("Generation")
        self.ax.set_ylabel("Fitness")
        self.ax.set_title("Best Fitness per Generation")
        self.ax.legend()
        self.ax.grid(True)
        self.ax.set_facecolor((224/255, 225/255, 225/255))

        self.canvas.draw()
        QtWidgets.QApplication.processEvents()

    # ========================================
    #   Таблица в массив
    # ========================================
    def table_to_array(self, table: QtWidgets.QTableWidget) -> list:
        rows = table.rowCount()
        cols = table.columnCount()
        data = []

        for i in range(rows):
            row_data = []
            for j in range(cols):
                item = table.item(i, j)
                value = item.text() if item else ''
                row_data.append(value)
            data.append(row_data)

        return data

    # ========================================
    #   Открыть файл
    # ========================================
    def open_txt_file(self):
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self.MainWindow, "Выберите текстовый файл", "",
                                                             "Text Files (*.txt)")
        if file_name:
            try:
                with open(file_name, "r", encoding="utf-8") as f:
                    text = f.read()
                if self.file_check(text) and self.table_check([item.split(' ') for item in text.split('\n')]):
                    self.error_label.setText("")
                    self.update_screen([item.split(' ') for item in text.split('\n')])
                else:
                    self.error_label.setText("Ошибка: Неверный формат поля")

            except Exception as e:
                QtWidgets.QMessageBox.warning(self.MainWindow, "Ошибка", f"Не удалось прочитать файл:\n{str(e)}")

    # ========================================
    #   Обновление загрузки
    # ========================================
    def update_progress_bar(self):
        min_rate = 243 - self.alg.best_fitness_values[0]
        best = min_rate - (243 - self.alg.best_fitness_values[-1])

        value = round((best / min_rate) * 100)
        self.progressBar.setValue(value)

    # ========================================
    #   Обновление загрузки
    # ========================================
    # def pause_alg(self):
    #     if self.is_pause:
    #         self.is_pause = False
    #         self.pause.setText("⏸")
    #     else:
    #         self.is_pause = True
    #         self.pause.setText("▶")

    def toggle_pause(self):

        self.is_pause = not self.is_pause

        if not self.is_pause:  # Если снимаем паузу
            if hasattr(self, 'generation_timer'):
                QTimer.singleShot(0, lambda: (
                    self.generation_timer.start(0),  # Запускаем таймер
                    self.pause.setText("⏸"),
                    self.start_btn.setEnabled(False),
                    self.start_btn.setStyleSheet("background-color: rgb(187, 188, 188);"
                                                "border-color: rgb(147, 147, 147); color: rgb(20, 21, 21); "
                                                "selection-color: rgb(255, 255, 255);"
                                                "selection-background-color: rgb(16, 81, 193);"
                                                "border-radius: 10px")
                ))

        else:
            self.pause.setText("▶")
            self.start_btn.setEnabled(True)
            self.start_btn.setStyleSheet("background-color: rgb(239, 240, 244);"
                                         "border-color: rgb(147, 147, 147); color: rgb(20, 21, 21); "
                                         "selection-color: rgb(255, 255, 255);"
                                         "selection-background-color: rgb(16, 81, 193);"
                                         "border-radius: 10px")

    # ========================================
    #   Проверка поля
    # ========================================
    def table_check(self, table):
        for i in range(9):
            for j in range(9):
                if not table[i][j].isdigit() and not table[i][j] == 'x':
                    return False
        return True

    def enter_check(self, table):
        for i in range(9):
            line = []
            column = []
            for j in range(9):
                if table[i][j].isdigit():
                    if not (0 < int(table[i][j]) <= 9):
                        return False
                    if table[i][j] not in line:
                        line.append(table[i][j])
                    else:
                        return False
                if table[j][i].isdigit():
                    if table[j][i] not in column:
                        column.append(table[j][i])
                    else:
                        return False
        return True

    def file_check(self, text: str) -> bool:
        lines = text.strip().splitlines()

        if len(lines) != 9:
            return False

        for i, line in enumerate(lines):
            parts = line.strip().split()
            if len(parts) != 9:
                return False
        return True

    # ========================================
    #   Обработчик функций
    # ========================================
    def functions(self):
        self.tableWidget.clicked.connect(lambda: self.on_row_clicked())
        self.start_btn.clicked.connect(self.start)
        self.one_step.clicked.connect(self.start_one)
        self.to_end.clicked.connect(self.start_until_the_end)
        self.pause.clicked.connect(self.toggle_pause)
        self.download_btn.clicked.connect(self.open_txt_file)

    # ========================================
    #   Подтверждение данных
    # ========================================
    def start(self):
        if self.is_start:
            print("Программа остановлена")
            self.start_btn.setText("Старт")
            if self.is_pause:
                self.is_pause = False
                self.pause.setText("⏸")  # Устанавливаем значок паузы
                self.pause.setStyleSheet("background-color: rgb(239, 240, 244);"
                                    "border-color: rgb(147, 147, 147); color: rgb(20, 21, 21); "
                                    "selection-color: rgb(255, 255, 255);"
                                    "selection-background-color: rgb(16, 81, 193);"
                                    "border-radius: 10px")
            clean_data()
            
            if hasattr(self, 'canvas'):
                self.graph_layout.removeWidget(self.canvas)
                self.canvas.setParent(None)

            self.screen.setText('')
            self.progressBar.setValue(0)
            self.tableWidget.setRowCount(0)
            self.to_end.setEnabled(False)
            self.one_step.setEnabled(False)
            self.pause.setEnabled(False)
            self.download_btn.setEnabled(True)
            self.spin_mutation.setReadOnly(False)
            self.enter_population_size.setReadOnly(False)
            self.enter_max.setReadOnly(False)
            self.tablescreen.setEnabled(True)
            self.to_end.setStyleSheet("background-color: rgb(187, 188, 188);"
                                      "border-color: rgb(147, 147, 147); color: rgb(20, 21, 21); "
                                      "selection-color: rgb(255, 255, 255);"
                                      "selection-background-color: rgb(16, 81, 193);"
                                      "border-radius: 10px")
            self.one_step.setStyleSheet("background-color: rgb(187, 188, 188);"
                                        "border-color: rgb(147, 147, 147); color: rgb(20, 21, 21);"
                                        "selection-color: rgb(255, 255, 255);"
                                        "selection-background-color: rgb(16, 81, 193);"
                                        "border-radius: 10px")
            self.pause.setStyleSheet("background-color: rgb(187, 188, 188);"
                                        "border-color: rgb(147, 147, 147); color: rgb(20, 21, 21);"
                                        "selection-color: rgb(255, 255, 255);"
                                        "selection-background-color: rgb(16, 81, 193);"
                                        "border-radius: 10px")
            self.download_btn.setStyleSheet("background-color: rgb(239, 240, 244);"
                                            "border-color: rgb(147, 147, 147); color: rgb(20, 21, 21); "
                                            "selection-color: rgb(255, 255, 255);"
                                            "selection-background-color: rgb(16, 81, 193);"
                                            "border-radius: 10px")
            self.label_bar.setStyleSheet("background-color: rgb(187, 188, 188);\n"
                                         "border-color: rgb(147, 147, 147);\n"
                                         "color: rgb(20, 21, 21);\n"
                                         "selection-color: rgb(255, 255, 255);\n"
                                         "selection-background-color: rgb(16, 81, 193);\n"
                                         "border-radius: 10px;")
            self.is_start = False
        else:
            is_correct = False

            while not is_correct:
                population_text = self.enter_population_size.text().strip()
                generations_text = self.enter_max.text().strip()
                table = self.table_to_array(self.tablescreen)

                if not generations_text:
                    self.error_label.setText("Ошибка: Поле 'Макс. поколений'\nне должно быть пустым.")
                    return

                if not population_text:
                    self.error_label.setText("Ошибка: Поле 'Размер популяции'\nне должно быть пустым.")
                    return

                if not self.table_check(table):
                    self.error_label.setText("Ошибка: Неверно задано поле")
                    return

                if not self.enter_check(table):
                    self.error_label.setText("Ошибка: Поле нарушает\nправила игры")
                    return

                is_correct = True


            print("Программа запущена")
            self.error_label.setText("")
            self.start_btn.setText("Стоп")
            clean_data()
            data_init()
            self.i = 0
            self.alg.main_permutation, self.alg.insert_list_indexes, self.alg.insert_list_symbols = ReadFromList(self.table_to_array(self.tablescreen))
            self.population_size = int(self.enter_population_size.text())
            self.alg.population = []
            self.alg.GeneratePopulation(self.population_size)
            self.generations = int(self.enter_max.text())
            self.p_mutation = float(self.spin_mutation.text().replace(',', '.'))
            self.update_table()

            self.figure = Figure(figsize=(10, 5), tight_layout=True)
            self.figure.patch.set_facecolor((224 / 255, 225 / 255, 225 / 255))
            self.canvas = FigureCanvas(self.figure)
            self.ax = self.figure.add_subplot(111)
            self.ax.set_facecolor((224 / 255, 225 / 255, 225 / 255))
            self.graph_layout.addWidget(self.canvas)
            self.canvas.show()

            self.to_end.setEnabled(True)
            self.one_step.setEnabled(True)
            self.download_btn.setEnabled(False)
            self.spin_mutation.setReadOnly(True)
            self.enter_population_size.setReadOnly(True)
            self.enter_max.setReadOnly(True)
            self.tablescreen.setEnabled(False)
            self.to_end.setStyleSheet("QPushButton {background-color: rgb(239, 240, 244);"
                                      "border-color: rgb(147, 147, 147); color: rgb(20, 21, 21); "
                                      "selection-color: rgb(255, 255, 255);"
                                      "selection-background-color: rgb(16, 81, 193);"
                                      "border-radius: 10px} QPushButton:pressed {background-color: rgb(200, 200, 200)}")
            self.one_step.setStyleSheet("QPushButton {background-color: rgb(239, 240, 244);"
                                        "border-color: rgb(147, 147, 147); color: rgb(20, 21, 21);"
                                        "selection-color: rgb(255, 255, 255);"
                                        "selection-background-color: rgb(16, 81, 193);"
                                        "border-radius: 10px}"
                                        "QPushButton:pressed {background-color: rgb(200, 200, 200)}")
            self.pause.setStyleSheet("QPushButton {background-color: rgb(239, 240, 244);"
                                     "border-color: rgb(147, 147, 147); color: rgb(20, 21, 21); "
                                     "selection-color: rgb(255, 255, 255);"
                                     "selection-background-color: rgb(16, 81, 193);"
                                     "border-radius: 10px} QPushButton:pressed {background-color: rgb(200, 200, 200)}")
            self.download_btn.setStyleSheet("background-color: rgb(187, 188, 188);"
                                            "border-color: rgb(147, 147, 147); color: rgb(20, 21, 21); "
                                            "selection-color: rgb(255, 255, 255);"
                                            "selection-background-color: rgb(16, 81, 193);"
                                            "border-radius: 10px")
            self.label_bar.setStyleSheet("background-color: rgb(239, 240, 244);\n"
                                         "border-color: rgb(147, 147, 147);\n"
                                         "color: rgb(20, 21, 21);\n"
                                         "selection-color: rgb(255, 255, 255);\n"
                                         "selection-background-color: rgb(16, 81, 193);\n"
                                         "border-radius: 10px;")
            self.is_start = True

    # ========================================
    #   Один шаг
    # ========================================
    def start_one(self):
        self.alg.one_iteration(self.population_size, self.p_mutation, self.i)
        self.update_progress_bar()
        self.update_table()
        data = read_data()
        label_text = format_9x9_square(str_to_field(data[str(self.i)][1]))
        self.screen.setText(label_text)
        self.plot_graph(self.data.get('best_fitness')[:int(self.i)])
        if self.alg.best_fitness_values[-1] == 243:
            print("Sudoku solved!")
            self.to_end.setEnabled(False)
            self.one_step.setEnabled(False)
            self.to_end.setStyleSheet("background-color: rgb(187, 188, 188);"
                                      "border-color: rgb(147, 147, 147); color: rgb(20, 21, 21); "
                                      "selection-color: rgb(255, 255, 255);"
                                      "selection-background-color: rgb(16, 81, 193);"
                                      "border-radius: 10px")
            self.one_step.setStyleSheet("background-color: rgb(187, 188, 188);"
                                        "border-color: rgb(147, 147, 147); color: rgb(20, 21, 21);"
                                        "selection-color: rgb(255, 255, 255);"
                                        "selection-background-color: rgb(16, 81, 193);"
                                        "border-radius: 10px")
        if self.i == self.generations:
            self.to_end.setEnabled(False)
            self.one_step.setEnabled(False)
            self.pause.setEnabled(False)
            self.to_end.setStyleSheet("background-color: rgb(187, 188, 188);"
                                      "border-color: rgb(147, 147, 147); color: rgb(20, 21, 21); "
                                      "selection-color: rgb(255, 255, 255);"
                                      "selection-background-color: rgb(16, 81, 193);"
                                      "border-radius: 10px")
            self.one_step.setStyleSheet("background-color: rgb(187, 188, 188);"
                                        "border-color: rgb(147, 147, 147); color: rgb(20, 21, 21);"
                                        "selection-color: rgb(255, 255, 255);"
                                        "selection-background-color: rgb(16, 81, 193);"
                                        "border-radius: 10px")
            self.pause.setStyleSheet("background-color: rgb(187, 188, 188);"
                                     "border-color: rgb(147, 147, 147); color: rgb(20, 21, 21);"
                                     "selection-color: rgb(255, 255, 255);"
                                     "selection-background-color: rgb(16, 81, 193);"
                                     "border-radius: 10px")
            self.label_bar.setStyleSheet("background-color: rgb(187, 188, 188);\n"
                                         "border-color: rgb(147, 147, 147);\n"
                                         "color: rgb(20, 21, 21);\n"
                                         "selection-color: rgb(255, 255, 255);\n"
                                         "selection-background-color: rgb(16, 81, 193);\n"
                                         "border-radius: 10px;")

        self.i += 1

    # ========================================
    #   До результата
    # ========================================
    def start_until_the_end(self):
        self.pause.setEnabled(True)
        self.start_btn.setEnabled(False)
        self.start_btn.setStyleSheet("background-color: rgb(187, 188, 188);"
                                  "border-color: rgb(147, 147, 147); color: rgb(20, 21, 21); "
                                  "selection-color: rgb(255, 255, 255);"
                                  "selection-background-color: rgb(16, 81, 193);"
                                  "border-radius: 10px")

        self.is_pause = False
        self.pause.setText("⏸")
        self.pause.setStyleSheet("background-color: rgb(239, 240, 244);"
                               "border-color: rgb(147, 147, 147); color: rgb(20, 21, 21); "
                               "selection-color: rgb(255, 255, 255);"
                               "selection-background-color: rgb(16, 81, 193);"
                               "border-radius: 10px")

        if not hasattr(self, 'generation_timer'):
            self.generation_timer = QTimer()
            self.generation_timer.timeout.connect(self._process_generation)

        self.current_generation = self.i
        self.generation_timer.start(0)

    def _process_generation(self):
        if self.is_pause:
            self.generation_timer.stop()
            return

        self.alg.one_iteration(self.population_size, self.p_mutation, self.i)

        if (self.i >= self.generations or
                self.alg.best_fitness_values[-1] == 243):
            self._finish_algorithm()
            return

        self.update_progress_bar()
        self.update_table()
        data = read_data()
        label_text = format_9x9_square(str_to_field(data[str(self.i)][1]))
        self.screen.setText(label_text)
        self.plot_graph(self.data.get('best_fitness')[:int(self.i)])

        self.i += 1

    def _finish_algorithm(self):

        self.generation_timer.stop()
        # self.i = self.current_generation

        print("Sudoku solved!")
        self.update_progress_bar()
        self.update_table()
        data = read_data()
        label_text = format_9x9_square(str_to_field(data[str(self.i)][1]))
        self.screen.setText(label_text)
        self.plot_graph(self.data.get('best_fitness')[:int(self.i)])

        self.to_end.setEnabled(False)
        self.one_step.setEnabled(False)
        self.pause.setEnabled(False)
        self.start_btn.setEnabled(True)
        self.start_btn.setStyleSheet("background-color: rgb(239, 240, 244);"
                                     "border-color: rgb(147, 147, 147); color: rgb(20, 21, 21); "
                                     "selection-color: rgb(255, 255, 255);"
                                     "selection-background-color: rgb(16, 81, 193);"
                                     "border-radius: 10px")
        self.to_end.setStyleSheet("background-color: rgb(187, 188, 188);"
                                  "border-color: rgb(147, 147, 147); color: rgb(20, 21, 21); "
                                  "selection-color: rgb(255, 255, 255);"
                                  "selection-background-color: rgb(16, 81, 193);"
                                  "border-radius: 10px")
        self.one_step.setStyleSheet("background-color: rgb(187, 188, 188);"
                                    "border-color: rgb(147, 147, 147); color: rgb(20, 21, 21);"
                                    "selection-color: rgb(255, 255, 255);"
                                    "selection-background-color: rgb(16, 81, 193);"
                                    "border-radius: 10px")
        self.pause.setStyleSheet("background-color: rgb(187, 188, 188);"
                                 "border-color: rgb(147, 147, 147); color: rgb(20, 21, 21);"
                                 "selection-color: rgb(255, 255, 255);"
                                 "selection-background-color: rgb(16, 81, 193);"
                                 "border-radius: 10px")
        self.label_bar.setStyleSheet("background-color: rgb(187, 188, 188);\n"
                                     "border-color: rgb(147, 147, 147);\n"
                                     "color: rgb(20, 21, 21);\n"
                                     "selection-color: rgb(255, 255, 255);\n"
                                     "selection-background-color: rgb(16, 81, 193);\n"
                                     "border-radius: 10px;")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setup_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
