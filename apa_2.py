from typing import List


class Edge:
    node_1 = ""
    node_2 = ""

    def __init__(self, n_1, n_2):
        self.node_1 = n_1
        self.node_2 = n_2

    def has_nodes(self, n_1, n_2):
        if self.node_1 == n_1 and self.node_2 == n_2:
            return True
        if self.node_1 == n_2 and self.node_2 == n_1:
            return True
        return False

    def concat_nodes(self):
        return self.node_1 + self.node_2

    def replace_node(self, n_1, n_2, new_node):
        if self.node_1 == n_1:
            self.node_1 = new_node
        if self.node_1 == n_2:
            self.node_1 = new_node
        if self.node_2 == n_1:
            self.node_2 = new_node
        if self.node_2 == n_2:
            self.node_2 = new_node



import numpy as np

import copy


def MCMinCut(graph: List[Edge]):
    i = 9
    g = copy.deepcopy(graph)
    while i > 2:
        edge = g.pop(np.random.randint(0, len(g) - 1))
        n_1 = edge.node_1
        n_2 = edge.node_2
        new_vertex = edge.concat_nodes()

        new_graph = []
        for e in g:
            if not e.has_nodes(n_1, n_2):
                e.replace_node(n_1, n_2, new_vertex)
                new_graph.append(e)

        g = new_graph

        i -= 1

    return len(g)


if __name__ == '__main__':
    nodes = ["A", "B", "C", "D", "E", "F", "G", "H"]

    GRAPH = [
        Edge("A", "B"),
        Edge("A", "E"),
        Edge("A", "H"),
        Edge("A", "D"),
        Edge("A", "C"),

        Edge("B", "E"),
        Edge("B", "I"),
        Edge("B", "F"),
        Edge("B", "C"),

        Edge("C", "D"),
        Edge("C", "G"),
        Edge("C", "F"),

        Edge("D", "G"),
        Edge("D", "H"),

        Edge("E", "H"),
        Edge("E", "I"),

        Edge("F", "I"),
        Edge("F", "G"),

        Edge("G", "I"),
        Edge("G", "H"),

        Edge("H", "I"),
    ]

    file = open("result_rick.txt", "w")
    for j in range(100000):
        k = MCMinCut(GRAPH)
        file.write("{}\n".format(k))
    file.close()

