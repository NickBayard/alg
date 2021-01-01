from queue import Queue


class Vertex:
    def __init__(self):
        self.marked = False
        self.edge_to = None
        self.adj = []


class TopologicalSort:
    def __init__(self, num, edges=None):
        self.vertices = [Vertex() for _ in range(num)]
        self.stack = []  # append and pop
        self.cycle = Queue()
        if edges is not None:
            for source, dest in edges:
                self.add_edge(source, dest)

    def add_edge(self, source, dest):
        self.vertices[source].adj.append(dest)

    def sort(self):
        for source, v in enumerate(self.vertices):
            if not v.marked:
                self.dfs(source)
                self.stack.append(source)

    def dfs(self, source):
        v = self.vertices[source]
        v.marked = True

        for adj in v.adj:
            w = self.vertices[adj]
            if not w.marked:
                w.edge_to = source
                self.dfs(adj)
                self.stack.append(adj)

    def topo(self):
        while self.stack:
            yield self.stack.pop()
