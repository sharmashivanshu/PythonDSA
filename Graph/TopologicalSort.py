from collections import defaultdict


class MyGraph:
    def __init__(self, number_of_vertex):
        self.graph = defaultdict(list)
        self.number_of_vertex = number_of_vertex

    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def __topological_helper(self, vertex, visited: list, stack: list):
        visited.append(vertex)
        for edge in self.graph[vertex]:
            if edge not in visited:
                self.__topological_helper(edge, visited, stack)
        stack.insert(0, vertex)

    def topological_sort(self):
        visited = []
        stack = []
        for i in list(self.graph):
            if i not in visited:
                self.__topological_helper(i, visited, stack)
        print(stack)


my_graph = MyGraph(8)
my_graph.add_edge("A", "C")
my_graph.add_edge("C", "E")
my_graph.add_edge("E", "H")
my_graph.add_edge("E", "F")
my_graph.add_edge("F", "G")
my_graph.add_edge("B", "D")
my_graph.add_edge("B", "C")
my_graph.add_edge("D", "F")

my_graph.topological_sort()
