import random
from graph import Graph, Vertex
import numpy as np
from shapely.geometry import LineString, Point

def build_Cfree(width, height, obstacles):
    resolution = 1000  # определяет количество точек в сетке, которые мы используем для построения плоскости
    x = np.linspace(0, width, resolution)  # создает одномерный массив чисел, распределенных равномерно
    y = np.linspace(0, height, resolution)  # от 0 до width/hidht включительно, с кол-вом элементов, равным resoluton

    grid = []

    for i in range(resolution):
        for j in range(resolution):
            is_inside = False
            for obstacle in obstacles:
                x_center, y_center, radius = obstacle
                dist = np.sqrt((x[i] - x_center) ** 2 + (y[j] - y_center) ** 2)
                if dist <= radius:
                    is_inside = True
                    break
            if not is_inside:
                grid.append((x[i], y[j]))

    return grid


def RandomSample(Cfree):  # выбор случайной точки из списка кортежей Cfree
    return random.choice(Cfree)


def collisionFree(x1, y1, x2, y2, obstacles):  # проверяет пересекается ли отрезок с препятствиями
    line = LineString([(x1, y1), (x2, y2)])  # создает отрезок между заданными точками
    for obstacle in obstacles:
        x_center, y_center, radius = obstacle

        circle = Point(x_center, y_center).buffer(radius)  # Создание круга
        if line.intersects(circle):
            return False
    return True


def Near(G, X, k):
    distances = []  # Список для хранения расстояний от заданной вершины X до остальных вершин в графе G

    # Вычисление расстояний от X до каждой вершины в G
    for node in G:
        dist = np.sqrt((X.x - node.x) ** 2 + (X.y - node.y) ** 2)
        distances.append((node, dist))

    # Сортировка расстояний по возрастанию
    sorted_distances = sorted(distances, key=lambda x: x[1])

    # Возвращение k ближайших вершин к X
    return sorted_distances[:k]


def dijkstra(graph, start_vertex, goal_vertex):
    # Инициализация расстояний до всех вершин как бесконечность, кроме начальной
    distances = {vertex: float('infinity') for vertex in graph.vertices}
    distances[start_vertex] = 0  # Расстояние до начальной вершины устанавливается равным нулю

    # Копирование списка вершин графа для дальнейшей работы с ним
    unvisited_nodes = list(graph.vertices)

    # Хранение предыдущих вершин для восстановления пути
    previous_nodes = {}

    # Определение функции для поиска вершины с наименьшим расстоянием
    # def min_distance(distances, visited):
    #     return min([(vertex, distance) for vertex, distance in distances.items() if vertex not in visited], key=lambda x: x[1])


    # Пока есть непосещенные вершины
    while unvisited_nodes:
        current_vertex, current_distance = min(distances.items(), key=lambda x: x[1] if x[0] in unvisited_nodes else float('inf'))
        unvisited_nodes.remove(current_vertex)

        for neighbor, distance in current_vertex.neighbors.items():
            tentative_value = distances[current_vertex] + distance
            if tentative_value < distances[neighbor]:
                distances[neighbor] = tentative_value
                previous_nodes[neighbor] = current_vertex

        # Удаление текущей вершины из списка непосещенных вершин
    path = []
    current = goal_vertex
    while current is not None:
        path.insert(0, (current.x, current.y))
        current = previous_nodes.get(current)

    return distances[goal_vertex], path


def nearest_vertices(graph, point, k):
    distances = []

    for vertex in graph.vertices:
        distance = np.sqrt((point.x - vertex.x) ** 2 + (point.y - vertex.y) ** 2)
        distances.append((vertex, distance))

    sorted_distances = sorted(distances, key=lambda x: x[1])

    return [vertex for vertex, _ in sorted_distances[:k]]




def PRM(N, k, Qinit, Qgoal,obstacles):

    my_graph = Graph()  # Пустой граф

    Cfree = build_Cfree(1000, 1000, obstacles)  # Создание Cfree



    # Пока число вершин в графе G меньше, чем N
    while len(my_graph.vertices) < N:
        Qrand = RandomSample(Cfree)  # добавляем N сэмплов в граф
        vertex = Vertex(Qrand[0], Qrand[1])
        my_graph.add_vertex(vertex)

    for Q in my_graph.vertices:
        Qnear = Near(my_graph.vertices, Q, k)
        for i in Qnear:
            Qn = i[0]
            if Q != Qn and collisionFree(Q.x, Q.y, Qn.x, Qn.y, obstacles):
                my_graph.add_edge(Q, Qn, i[1])

        # Соединение начальной и конечной вершин с графом
    nearest_init = nearest_vertices(my_graph, Qinit, k)
    nearest_goal = nearest_vertices(my_graph, Qgoal, k)

    my_graph.add_vertex(Qinit)
    my_graph.add_vertex(Qgoal)

    for vertex in nearest_init:
        if vertex != Qinit and collisionFree(Qinit.x, Qinit.y, vertex.x, vertex.y, obstacles):
            my_graph.add_edge(Qinit, vertex, np.sqrt((Qinit.x - vertex.x) ** 2 + (Qinit.y - vertex.y) ** 2))

    for vertex in nearest_goal:
        if vertex != Qgoal and collisionFree(Qgoal.x, Qgoal.y, vertex.x, vertex.y, obstacles):
            my_graph.add_edge(Qgoal, vertex, np.sqrt((Qgoal.x - vertex.x) ** 2 + (Qgoal.y - vertex.y) ** 2))
    print( [(i.x, i.y) for i in my_graph.vertices])
    return dijkstra(my_graph, Qinit, Qgoal), my_graph.vertices

# print(PRM(1000,100,Vertex(0,0),Vertex(1000,1000),[(50,50,10)]))





    # print(i.x, i.y)
    # print('neighbors:')
    # # for j in i.neighbors:
    # #     print(j.x, j.y)
    # print(len(i.neighbors))
    # print('--------------------------------------')

