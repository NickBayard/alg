from graph.undirected import Graph
from queue import Queue


class DiGraph(Graph):
    def add_edge(self, source:int, dest:int):
        if dest not in self.adj[source]:
            self.adj[source].append(dest)
            self.num_e += 1


class DirectedCycle:
    def __init__(self, graph):
        self.graph = graph
        self.marked = [False] * graph.num_v
        self.edge_to = [None] * graph.num_v
        self.cycle = Queue()

    def search(self):
        for source in range(self.graph.num_v):
            if not self.marked[source]:
                self.dfs(source)

    def dfs(self, source):
        self.marked[source] = True
        for v in self.graph.adjacent(source):
            if not self.cycle.empty():
                return
            if v != source:
                if self.marked[v]:
                    # cycle
                    self.cycle.put(v)
                    vertex = source
                    while vertex != v:
                        self.cycle.put(vertex)
                        vertex = self.edge_to[vertex]
                else:
                    self.edge_to[v] = source
                    self.marked[v] = True
                    self.dfs(v)
