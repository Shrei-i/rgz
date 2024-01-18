

from PyQt5 import QtCore,  QtWidgets
from PyQt5.QtCore import Qt, QPointF, QSizeF
from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtWidgets import QGraphicsScene, QMessageBox, QGraphicsEllipseItem, QGraphicsRectItem, QGraphicsItem, \
    QGraphicsLineItem, QPushButton, QLineEdit, QFileDialog

from algoritm import PRM
from graph import Vertex
import pickle

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1900, 1035))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridLayoutWidget.sizePolicy().hasHeightForWidth())
        self.gridLayoutWidget.setSizePolicy(sizePolicy)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(11, -1, 0, 0)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.line_init = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.line_init.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_init.sizePolicy().hasHeightForWidth())
        self.line_init.setSizePolicy(sizePolicy)
        self.line_init.setText("")
        self.line_init.setPlaceholderText("Qinit в формате (x, y)")
        self.line_init.setObjectName("line_init")
        self.horizontalLayout_3.addWidget(self.line_init)
        self.btn_init = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_init.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_init.sizePolicy().hasHeightForWidth())
        self.btn_init.setSizePolicy(sizePolicy)
        self.btn_init.setObjectName("btn_init")
        self.horizontalLayout_3.addWidget(self.btn_init)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.line_goal = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.line_goal.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_goal.sizePolicy().hasHeightForWidth())
        self.line_goal.setSizePolicy(sizePolicy)
        self.line_goal.setObjectName("line_goal")
        self.horizontalLayout_2.addWidget(self.line_goal)
        self.btn_goal = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_goal.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_goal.sizePolicy().hasHeightForWidth())
        self.btn_goal.setSizePolicy(sizePolicy)
        self.btn_goal.setObjectName("btn_goal")
        self.horizontalLayout_2.addWidget(self.btn_goal)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.line_obstacles = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.line_obstacles.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_obstacles.sizePolicy().hasHeightForWidth())
        self.line_obstacles.setSizePolicy(sizePolicy)
        self.line_obstacles.setObjectName("line_obstacles")
        self.horizontalLayout_4.addWidget(self.line_obstacles)
        self.btn_obstacles = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_obstacles.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_obstacles.sizePolicy().hasHeightForWidth())
        self.btn_obstacles.setSizePolicy(sizePolicy)
        self.btn_obstacles.setObjectName("btn_obstacles")
        self.horizontalLayout_4.addWidget(self.btn_obstacles)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.btn_graph = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_graph.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_graph.sizePolicy().hasHeightForWidth())
        self.btn_graph.setSizePolicy(sizePolicy)
        self.btn_graph.setMinimumSize(QtCore.QSize(50, 100))
        _translate = QtCore.QCoreApplication.translate


        self.btn_delete_init = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_delete_init.setEnabled(True)
        self.btn_delete_init.setSizePolicy(sizePolicy)
        self.btn_delete_init.setMinimumSize(QtCore.QSize(0, 100))
        self.btn_delete_init.setObjectName("btn_delete_init")
        self.btn_delete_init.setText(_translate("MainWindow", "Удалить начальную точку"))
        self.horizontalLayout_3.addWidget(self.btn_delete_init)

        self.btn_delete_goal = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_delete_goal.setEnabled(True)
        self.btn_delete_goal.setSizePolicy(sizePolicy)
        self.btn_delete_goal.setMinimumSize(QtCore.QSize(0, 100))
        self.btn_delete_goal.setObjectName("btn_delete_goal")
        self.btn_delete_goal.setText(_translate("MainWindow", "Удалить конечную точку"))
        self.horizontalLayout_2.addWidget(self.btn_delete_goal)

        self.btn_save_obstacles = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_save_obstacles.setText(_translate("MainWindow", "Сохранить препятствия"))
        self.btn_save_obstacles.setEnabled(True)
        self.btn_save_obstacles.setSizePolicy(sizePolicy)
        self.btn_save_obstacles.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_save_obstacles.setObjectName("btn_save_obstacles")
        self.horizontalLayout_4.addWidget(self.btn_save_obstacles)

        self.btn_delete_obstacles = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_delete_obstacles.setEnabled(True)
        self.btn_delete_obstacles.setSizePolicy(sizePolicy)
        self.btn_delete_obstacles.setMinimumSize(QtCore.QSize(0, 100))
        self.btn_delete_obstacles.setObjectName("btn_delete_obstacles")
        self.btn_delete_obstacles.setText(_translate("MainWindow", "Удалить препятствие"))
        self.horizontalLayout_4.addWidget(self.btn_delete_obstacles)

        self.line_N = QLineEdit(self.gridLayoutWidget)
        self.line_N.setPlaceholderText("Число семплов (N=100)")
        self.verticalLayout.addWidget(self.line_N)

        self.line_k = QLineEdit(self.gridLayoutWidget)
        self.line_k.setPlaceholderText("число ближайших вершин к рассмотрению (k=30)")
        self.verticalLayout.addWidget(self.line_k)

        self.btn_shortest_path = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_shortest_path.setEnabled(True)
        self.btn_shortest_path.setSizePolicy(sizePolicy)
        self.btn_shortest_path.setMinimumSize(0, 100)
        self.btn_shortest_path.setObjectName("btn_shortest_path")
        self.verticalLayout.addWidget(self.btn_shortest_path)
        self.btn_shortest_path.setText(_translate("MainWindow", "Найти кратчайший путь"))
        self.btn_download = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_download.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_download.sizePolicy().hasHeightForWidth())
        self.btn_download.setSizePolicy(sizePolicy)
        self.btn_download.setMinimumSize(QtCore.QSize(0, 100))
        self.btn_download.setObjectName("btn_download")
        self.verticalLayout.addWidget(self.btn_download)
        self.btn_save = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_save.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QtCore.QSize(0, 100))
        self.btn_save.setObjectName("btn_save")
        self.verticalLayout.addWidget(self.btn_save)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 2)
        self.graphicsView = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QtCore.QSize(0, 0))
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 100)
        self.gridLayout.setColumnStretch(1, 45)
        MainWindow.setCentralWidget(self.centralwidget)

        self.btn_reset = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_reset.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_reset.sizePolicy().hasHeightForWidth())
        self.btn_reset.setSizePolicy(sizePolicy)
        self.btn_reset.setMinimumSize(QtCore.QSize(0, 100))
        self.btn_reset.setObjectName("btn_reset")
        self.btn_reset.setText("Сброс")
        self.verticalLayout.addWidget(self.btn_reset)

        self.label_path_length = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_path_length.setObjectName("label_path_length")
        self.verticalLayout.addWidget(self.label_path_length)

        self.btn_delete_init.clicked.connect(self.delete_init_point)
        self.btn_delete_goal.clicked.connect(self.delete_goal_point)
        self.btn_delete_obstacles.clicked.connect(self.delete_obstacle)
        self.btn_reset.clicked.connect(self.reset_data)
        self.btn_save.clicked.connect(self.save_scene)
        self.btn_download.clicked.connect(self.load_scene)
        self.btn_obstacles.clicked.connect(self.show_obstacles)
        self.btn_save_obstacles.clicked.connect(self.update_centers)
        self.btn_save_obstacles.clicked.connect(self.update_centers)
        self.btn_shortest_path.clicked.connect(self.find_shortest_path)
        self.btn_init.clicked.connect(self.show_init_points)
        self.btn_goal.clicked.connect(self.show_goal_points)

        self.path_line = None
        self.edge_lines = []
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.path = []
        self.obstacles = []
        self.init = []
        self.goal = []
        self.scene = MyGraphicsSceneWithBorder(0, 0, 1000, 1000)  # Начальный размер сцены
        self.graphicsView.setScene(self.scene)
        self.graph_data = []
        # Событие для отображения точек начала и конца
        self.flag_init = True
        self.flag_goal = True
        self.N = 0
        self.k = 0

    def initialize_scene(self):
        self.scene.clear()
        self.scene = MyGraphicsSceneWithBorder(0, 0, 1000, 1000)
        self.graphicsView.setScene(self.scene)

    def update_N_and_k(self):
        self.N = int(self.line_N.text()) if self.line_N.text() else 100
        self.k = int(self.line_k.text()) if self.line_k.text() else 30
    def show_init_points(self):
        init_text = self.line_init.text()
        try:
            if self.flag_init:
                x_init, y_init = map(float, init_text.replace('(', '').replace(')', '').split(','))


                radius = 5.0
                point_init = QGraphicsEllipseItem(x_init - radius, y_init - radius, 2 * radius, 2 * radius)
                point_init.setBrush(Qt.red)
                self.scene.addItem(point_init)
                self.init.append((x_init,y_init))
                self.flag_init=False

            self.update_N_and_k()

        except ValueError as e:
            print('Error:', e)  # Добавьте это сообщение
            QMessageBox.warning(MainWindow, "Ошибка", "Неверный формат координат")



    def show_goal_points(self):
        goal_text = self.line_goal.text()
        try:
            if self.flag_goal:
                x_goal, y_goal = map(float, goal_text.replace('(', '').replace(')', '').split(','))
                radius = 5.0
                point_goal = QGraphicsEllipseItem(x_goal - radius, y_goal - radius, 2 * radius, 2 * radius)
                point_goal.setBrush(Qt.blue)
                self.scene.addItem(point_goal)
                self.goal.append((x_goal,y_goal))
                self.flag_goal=False
            self.update_N_and_k()


        except ValueError as e:
            print('Error:', e)
            QMessageBox.warning(MainWindow, "Ошибка", "Неверный формат координат")




    def show_obstacles(self):
        obstacle_text = self.line_obstacles.text()
        try:
            radius = float(obstacle_text)
            obstacle = EditableEllipseItem(0,0, radius)
            obstacle.setPos(0, 0)
            obstacle.update_center()
            self.scene.addItem(obstacle)
            obstacle.update_center()
            self.obstacles.append((obstacle, radius))
            print(self.obstacles)
        except ValueError as e:
            print('Error:', e)  # Добавьте это сообщение
            QMessageBox.warning(MainWindow, "Ошибка", "Неверный формат координат")

    def update_centers(self):
        for i, obstacle in enumerate(self.obstacles):
            obstacle[0].update_center()  # обновляем координаты центра для каждого элемента
            self.obstacles[i] = (obstacle[0], obstacle[0].radius)
            print(obstacle[0].center_x, obstacle[0].center_y, obstacle[0].radius)

    def find_shortest_path(self):
        try:
            self.update_N_and_k()
            self.scene.removeItem(self.label_path_length.clear())
            for i in self.edge_lines:
                self.scene.removeItem(i)
            for item in self.scene.items():
                if isinstance(item, QGraphicsEllipseItem) and item.brush().color() == Qt.black:
                    self.scene.removeItem(item)
            self.label_path_length.clear()
            Qinit = self.init[0]
            Qgoal = self.goal[0]
            obstacles = [(obstacle[0].center_x, obstacle[0].center_y, obstacle[1]) for obstacle in self.obstacles]

            f = PRM(self.N, self.k, Vertex(Qinit[0], Qinit[1]), Vertex(Qgoal[0], Qgoal[1]), obstacles)
            distances, path, graph = f[0][0], f[0][1], f[1]

            self.graph_data = graph
            path = [QPointF(point[0], point[1]) for point in path]

            for vertex in graph:
                x1, y1 = vertex.x, vertex.y
                for neighbor, weight in vertex.neighbors.items():
                    x2, y2 = neighbor.x, neighbor.y
                    edge_line = QGraphicsLineItem(x1, y1, x2, y2)
                    edge_line.setPen(QPen(Qt.gray))
                    self.edge_lines.append(edge_line)
                    self.scene.addItem(edge_line)
            self.graphicsView.setScene(self.scene)
            for i in range(len(path) - 1):
                x1, y1 = path[i].x(), path[i].y()
                x2, y2 = path[i + 1].x(), path[i + 1].y()
                self.show_point(x1, y1, Qt.black)
                path_line = QGraphicsLineItem(x1, y1, x2, y2)
                pen = QPen(Qt.blue)
                pen.setWidth(2)
                path_line.setPen(pen)
                self.scene.addItem(path_line)
            self.label_path_length.setText(f"Длина кратчайшего пути: {distances}")
            self.path = path
        except Exception as e:
            print(e)
            self.show_warning_message(f"Невозможно построить путь")


    def show_warning_message(self,message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setText(message)
        msg_box.setWindowTitle("Ошибка")
        msg_box.exec_()

    def show_point(self, x, y, color):
        radius = 5.0
        point = QGraphicsEllipseItem(x - radius, y - radius, 2 * radius, 2 * radius)
        point.setBrush(color)
        self.scene.addItem(point)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_init.setText(_translate("MainWindow", "Сохранить"))
        self.line_goal.setPlaceholderText(_translate("MainWindow", "Qgoal в формате (x,y)"))
        self.btn_goal.setText(_translate("MainWindow", "Сохранить"))
        self.line_obstacles.setPlaceholderText(_translate("MainWindow", "Введите диаметр препятствия"))
        self.btn_obstacles.setText(_translate("MainWindow", "Добавить"))
        self.btn_download.setText(_translate("MainWindow", "Загрузить сцену из файла"))
        self.btn_save.setText(_translate("MainWindow", "Сохранить сцену в файл"))

    def delete_init_point(self):
        if self.init:
            x, y = self.init.pop()
            items = self.scene.items()
            for item in items:
                if isinstance(item, QGraphicsEllipseItem) and item.rect().contains(QPointF(x, y)):
                    self.scene.removeItem(item)
                    self.flag_init = True

    def delete_goal_point(self):
        if self.goal:
            x, y = self.goal.pop()
            items = self.scene.items()
            for item in items:
                if isinstance(item, QGraphicsEllipseItem) and item.rect().contains(QPointF(x, y)):
                    self.scene.removeItem(item)
                    self.flag_goal = True

    def delete_obstacle(self):
        if self.obstacles:
            obstacle, _ = self.obstacles.pop()
            self.scene.removeItem(obstacle)

    def reset_data(self):
        # Очистите данные из GUI
        self.edge_lines.clear()
        self.line_init.clear()
        self.line_goal.clear()
        self.line_N.clear()
        self.line_k.clear()
        self.line_obstacles.clear()
        self.init = []
        self.goal = []
        self.obstacles = []
        self.flag_init = True
        self.flag_goal = True
        self.scene.clear()
        self.scene = MyGraphicsSceneWithBorder(0, 0, 1000, 1000)
        self.graphicsView.setScene(self.scene)
        self.label_path_length.clear()

    def save_scene(self):
        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            file_name, _ = QFileDialog.getSaveFileName(None, "Сохранить сцену", "", "Pickle Files (*.pkl);;All Files (*)",
                                                       options=options)

            if file_name:
                scene_data = {
                    "init": self.init,
                    "goal": self.goal,
                    "obstacles": [(obstacle[0].center_x, obstacle[0].center_y, obstacle[1]) for obstacle in
                                  self.obstacles],
                    "path": [(point.x(), point.y()) for point in self.path] if self.path else None,
                    "path_length": self.label_path_length.text() if self.label_path_length.text() else None,
                    "graph": self.graph_data,
                    "N": self.N,
                    "k": self.k,

                }

                with open(file_name, "wb") as f:
                    pickle.dump(scene_data, f)

        except Exception as e:
            print('Error saving scene:', e)
            self.show_warning_message("Невозможно сохранить сцену")

    def load_scene(self):
        try:
            file_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Открыть сцену", "", "Scene Files (*.pkl)")
            if file_path:
                with open(file_path, "rb") as f:
                    scene_data = pickle.load(f)


                self.scene.clear()
                self.scene = MyGraphicsSceneWithBorder(0, 0, 1000, 1000)
                self.graphicsView.setScene(self.scene)


                self.N = scene_data.get("N")
                self.k = scene_data.get("k")

                self.line_N.setText(str(self.N))
                self.line_k.setText(str(self.k))

                for x, y in scene_data["init"]:
                    self.show_point(x, y, Qt.red)
                    self.init = [(x,y)]
                for x, y in scene_data["goal"]:
                    self.show_point(x, y, Qt.blue)
                    self.goal = [(x, y)]
                for x, y, radius in scene_data["obstacles"]:
                    obstacle = EditableEllipseItem(0, 0, radius)
                    obstacle.setPos(x, y)
                    obstacle.update_center()
                    self.scene.addItem(obstacle)
                    self.obstacles.append((obstacle, radius))

                if scene_data["path"]:
                    self.path = [QPointF(point[0], point[1]) for point in scene_data["path"]]
                    for i in range(len(self.path) - 1):
                        x1, y1 = self.path[i].x(), self.path[i].y()
                        x2, y2 = self.path[i + 1].x(), self.path[i + 1].y()
                        path_line = QGraphicsLineItem(x1, y1, x2, y2)
                        self.show_point(x1, y1, Qt.black)
                        pen = QPen(Qt.blue)
                        pen.setWidth(2)  # Установите нужную толщину линии
                        path_line.setPen(pen)
                        self.scene.addItem(path_line)
                path_length = scene_data.get("path_length")
                if path_length:
                    self.label_path_length.setText(path_length)
                for vertex in scene_data["graph"]:
                    x1, y1 = vertex.x, vertex.y

                    for neighbor, weight in vertex.neighbors.items():
                        x2, y2 = neighbor.x, neighbor.y
                        edge_line = QGraphicsLineItem(x1, y1, x2, y2)
                        self.edge_lines.append(edge_line)
                        edge_line.setPen(QPen(Qt.gray))
                        self.scene.addItem(edge_line)
                self.update_N_and_k()


        except Exception as e:
            print('Error loading scene:', e)
            self.show_warning_message("Невозможно открыть сцену")

class MyGraphicsSceneWithBorder(QGraphicsScene):
    def __init__(self, x, y, width, height):
        super(MyGraphicsSceneWithBorder, self).__init__(x, y, width, height)
        self.setSceneRect(x, y, width, height)

        # Создаем границу сцены
        border_rect = QGraphicsRectItem(x, y, width, height)
        border_rect.setPen(Qt.black)  # Задаем цвет границы
        self.addItem(border_rect)

class EditableEllipseItem(QGraphicsEllipseItem):
    def __init__(self, x, y, radius):
        super(EditableEllipseItem, self).__init__(x - radius, y - radius, 2 * radius, 2 * radius)
        self.setBrush(Qt.color0)
        self.setFlag(QGraphicsEllipseItem.ItemIsMovable)
        self.radius = radius
        self.update_center()

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionChange:
            self.update_center()  # Обновление центра при перемещении
        return super(EditableEllipseItem, self).itemChange(change, value)

    def update_center(self):
        self.center_x = self.x()
        self.center_y = self.y()
        print(f"New center coordinates: ({self.center_x}, {self.center_y})")

    def mousePressEvent(self, event):
        self.update_center()  # Обновление центра при клике на элемент
        return super(EditableEllipseItem, self).mousePressEvent(event)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



