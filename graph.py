class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbors = {}  # Используем словарь для хранения смежных вершин и веса ребра
        self.previous = None
    def add_neighbor(self, vertex, weight=1):  # weight по умолчанию равен 1, если не задан
        self.neighbors[vertex] = weight


class Graph:
    def __init__(self):
        self.vertices = []

    def add_vertex(self, vertex):
        self.vertices.append(vertex)


    def add_edge(self, vertex1, vertex2, weight=1):
        vertex1.add_neighbor(vertex2, weight)
        vertex2.add_neighbor(vertex1, weight)
