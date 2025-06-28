from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets


class GUIWindow(object):
    def setup_ui(self, main_window):

        # --- Параметры окна ---
        main_window.setObjectName("MainWindow")
        main_window.resize(500, 500)
        main_window.setMinimumSize(QtCore.QSize(500, 500))
        main_window.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        main_window.setFont(font)
        main_window.setStyleSheet("""
            background-color: rgb(30, 32, 34);
            selection-color: rgb(65, 66, 72);
            selection-background-color: rgb(33, 35, 39);
            alternate-background-color: rgb(23, 24, 25);
            color: rgb(140, 142, 156);
        """)
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("centralwidget")

        # --- Заголовок окна ---
        self.label = QtWidgets.QLabel(self.central_widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 501, 31))
        self.label.setStyleSheet("background-color: rgb(15, 18, 19);")
        self.label.setText("")

        # --- Название блока параметров ---
        self.label_name = QtWidgets.QLabel(self.central_widget)
        self.label_name.setGeometry(QtCore.QRect(10, 325, 481, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")

        # --- Вкладки ---
        self.Tabs = QtWidgets.QTabWidget(self.central_widget)
        self.Tabs.setGeometry(QtCore.QRect(0, 9, 500, 311))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Tabs.setFont(font)
        self.Tabs.setStyleSheet("""
            border-top-color: transparent;
            selection-color: rgb(93, 95, 109);
            selection-background-color: rgb(51, 67, 70);
            background-color: rgb(15, 18, 19);
        """)
        self.Tabs.setObjectName("Tabs")

        # --- Вкладка: Главная ---
        self.main = QtWidgets.QWidget()
        self.main.setObjectName("main")

        # Таблица
        self.tableWidget = QtWidgets.QTableWidget(self.main)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 200, 270))
        self.tableWidget.setStyleSheet("""
            border-color: rgb(30, 32, 34);
            background-color: rgb(22, 23, 25);
            color: rgb(140, 142, 156);
        """)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["№", "Данные"])
        self.tableWidget.setColumnWidth(0, 30)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # Поле отображения содержимого
        self.screen = QtWidgets.QLabel(self.main)
        self.screen.setGeometry(QtCore.QRect(220, 10, 270, 270))
        font.setPointSize(20)
        font.setBold(False)
        font.setUnderline(True)
        self.screen.setFont(font)
        self.screen.setStyleSheet("background-color: rgb(22, 23, 25);")
        self.screen.setAlignment(QtCore.Qt.AlignCenter)
        self.screen.setObjectName("screen")

        self.Tabs.addTab(self.main, "Главная")

        # --- Вкладка: График ---
        self.graph = QtWidgets.QWidget()
        self.graph.setObjectName("graph")
        self.graph_layout = QtWidgets.QVBoxLayout(self.graph)
        self.graph_layout.setContentsMargins(10, 10, 10, 10)
        self.Tabs.addTab(self.graph, "График")

        # --- Панель параметров ---
        self.gridLayoutWidget = QtWidgets.QWidget(self.central_widget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 350, 501, 115))
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setHorizontalSpacing(20)

        # Метки и поля
        self.label_field = QtWidgets.QLabel("Размер поля")
        self.label_population = QtWidgets.QLabel("Размер популяции")
        self.label_crossover = QtWidgets.QLabel("Вероятность скрещивания")
        self.label_mutation = QtWidgets.QLabel("Вероятность мутации")
        self.label_max = QtWidgets.QLabel("Макс. кол-во поколений")

        self.enter_field_size = QtWidgets.QLineEdit()
        self.enter_population_size = QtWidgets.QLineEdit()
        self.spin_crossover = QtWidgets.QDoubleSpinBox()
        self.spin_mutation = QtWidgets.QDoubleSpinBox()
        self.enter_max = QtWidgets.QLineEdit()

        # Стили
        style_input = """
            background-color: rgb(51, 53, 58);
            border-color: transparent;
            color: rgb(93, 151, 249);
        """
        for widget in [self.enter_field_size, self.enter_population_size, self.enter_max,
                       self.spin_crossover, self.spin_mutation]:
            widget.setStyleSheet(style_input)

        # Добавление в сетку
        self.gridLayout.addWidget(self.label_field, 0, 0)
        self.gridLayout.addWidget(self.enter_field_size, 0, 1)
        self.gridLayout.addWidget(self.label_crossover, 0, 2)
        self.gridLayout.addWidget(self.spin_crossover, 0, 3)

        self.gridLayout.addWidget(self.label_population, 1, 0)
        self.gridLayout.addWidget(self.enter_population_size, 1, 1)
        self.gridLayout.addWidget(self.label_mutation, 1, 2)
        self.gridLayout.addWidget(self.spin_mutation, 1, 3)

        self.gridLayout.addWidget(self.label_max, 3, 0)
        self.gridLayout.addWidget(self.enter_max, 3, 1)

        # --- Кнопка запуска ---
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.central_widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 460, 501, 41))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        spacer_left = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        spacer_right = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.start_btn = QtWidgets.QPushButton("Запуск")
        self.start_btn.setFixedSize(150, 25)
        self.start_btn.setStyleSheet("background-color: rgb(38, 40, 44);")

        self.horizontalLayout.addItem(spacer_left)
        self.horizontalLayout.addWidget(self.start_btn)
        self.horizontalLayout.addItem(spacer_right)

        # --- Завершение интерфейса ---
        main_window.setCentralWidget(self.central_widget)
        self.translate_ui(main_window)
        self.Tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)

        # --- Вызов функции обработчиков ---
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
    def translate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "ГА Судоку"))
        self.screen.setText(_translate("MainWindow", "\n".join(["0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0"] * 9)))
        self.label_name.setText(_translate("MainWindow", "Задайте параметры"))

    # --- Обработчик функций ---
    def functions(self):
        self.tableWidget.clicked.connect(lambda: self.on_row_clicked())
        self.start_btn.clicked.connect(lambda: self.start())

    # --- Обработчик запуска ---
    def start(self):
        print("Запущено")

        x = list(range(10))
        y1 = [i ** 2 for i in x]
        y2 = [i * 3 for i in x]
        self.plot_graph(x, y1, y2)


data = {
    "1": ["data", "1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9\n" * 9],
    "2": ["data", "9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1\n" * 9],
    "3": ["data", "0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0\n" * 9]
}

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GUIWindow()
    ui.setup_ui(MainWindow)
    ui.update_table(data)
    MainWindow.show()
    sys.exit(app.exec_())